# encoding: utf-8
import re
import os
import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.model as model
import ckan.logic.validators as validators
from ckan.common import _





###############################
# MAP ICO_XXX TO DCAT METADATA
###############################
def converter_from_ico_to_dcat (key, data, errors, context):
    	
	#print key[-1]
	tmp = data[key]
	
	if key[-1]== 'ico_lingua': 
		key = ('language',) #MAP TO LANGUAGE
	
	elif key[-1]== 'ico_temporal_start':
		key = ('temporal_start',) #MAP TO TEMPORAL_START
	
	elif key[-1]== 'ico_temporal_end':
		key = ('temporal_end',) #MAP TO TEMPORAL_END
	
	elif key[-1]== 'ico_frequencza_aggiornamento':
		key = ('frequency',) #MAP TO FREQUENCY
	
	elif key[-1]== 'ico_conformsTo':
		key = ('conforms_to',) #MAP TO CONFORM
	
	elif key[-1]== 'ico_nome_ente_responsabile':
		key = ('holder_name',) #MAP TO RIGHTS HOLDER

	elif key[-1]== 'ico_nome_struttura_riferimento':
		key = ('publisher_name',) #MAP TO PUBLISHER (EDITOR)
	
	elif key[-1]== 'ico_isVersionOf':
		key = ('is_version_of',) #MAP TO VERSION
	
	elif key[-1]== 'identifier':		
		tmp = data[('name',)] # FIX IDENTIFIER


	#elif key[-1]== 'ico_rightsHolder':
	#	key = ('rightsHolder_url',) #MAP TO RIGHTS	
	
		
    	current_indexes = [k[1] for k in data.keys() if len(k) > 1 and k[0] == 'extras']
	
    	new_index = max(current_indexes) + 1 if current_indexes else 0

    	data[('extras', new_index, 'key')] = key[-1]
    	data[('extras', new_index, 'value')] = tmp 
	

		






#######################################################
# EXTENDO CONVERTITORE PER GESTIRE CAT E SOTTOCAT GEMET
# IN INPUT IN CONFLITTO COL VOCABOLARIO
#######################################
def gemet_converter(vocab):
    def callable(key, data, errors, context):
	#print key
	
	if isinstance(data.get(key), basestring): #######controllo se vocab o string
		#print "string"
		tmp= data.get(key)
		tmp= tmp.replace("[", "") # errore scrittura lista/string
		tmp= tmp.replace("]", "")
		tmp= tmp.replace("'", " ") # apostrofo non accettato nel vocabolario
	    	tmp= tmp.replace(",", "-") # non accetta la virgola
		tmp= tmp.replace("(", "-") # nemmeno parentesi
		tmp= tmp.replace(")", "-")
		new_tags = tmp.lower().split("; ")#############		
	else:
		#print "uni"
		tmp = data.get(key)
		new_tags=[]
		import unicodedata
		for t in tmp:
			tmp_tags=re.split(', |,', unicodedata.normalize('NFKD', t).encode('ascii','ignore'))
			for tag in tmp_tags:
				new_tags.append(tag.lower())
        if not new_tags:
            return
        if isinstance(new_tags, basestring):   
            new_tags = [new_tags]

        # get current number of tags
        n = 0
        for k in data.keys():
            if k[0] == 'tags':
                n = max(n, k[1] + 1) 

        v = model.Vocabulary.get(vocab)
        if not v:
            raise df.Invalid(_('Tag vocabulary "%s" does not exist') % vocab)
        context['vocabulary'] = v
	
        for tag in new_tags:
	    
	    tag = tag.replace("'", " ") # apostrofo non accettato nel vocabolario
	    tag = tag.replace(",", "-") # non accetta la virgola
	    tag = tag.replace("(", "-") # nemmeno parentesi
	    tag = tag.replace(")", "-")	
	   
            errore= validators.tag_in_vocabulary_validator(tag, context) #modified by FAST
	    #print errore
	    if errore:
		new_tags.remove(tag)


        for num, tag in enumerate(new_tags):
            data[('tags', num + n, 'name')] = tag
            data[('tags', num + n, 'vocabulary_id')] = v.id
	
    return callable
