import json
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic.action.get as get
import requests
from sqlalchemy import create_engine
from ckan.lib.base import BaseController, render
import unicodedata
import ckan.lib.helpers as h
from operator import itemgetter
import urllib2
from ckan.common import c




########################################################
# FILTERS QUERY SOLR
# filtra pkg in base alle organizzazioni dell'utente
# eventualmente aggiungere altri filtri qui
########################################################
def more_filters():
	org_utente = [org['name'] for org in h.organizations_available('read')]
	fq = '(capacity:"public"'
	for org in org_utente:
		fq += ' OR (capacity:"private" AND organization:"' + org + '")'
	fq += ')'
	fq += 'state:"active"'
	return fq


########################################################
# GET NUM DATASETS
# remember: admin sees all datasets!
########################################################
def get_numDatasets():
	# SOLR query
	fq = more_filters()  # filtra pkg in base alle organizzazioni dell'utente
	# fq += ' +dataset_type:dataset'
	data_dict = {'fq': fq}
	diz = h.get_action('package_search', data_dict)
	num_pkg = diz['count']
	return num_pkg


########################################################
# GET NUM GRUPPI
########################################################
def get_numGroups():
	count =0
	diz = h.get_action('group_list')
	count = len(diz)
	return count


########################################################
# GET NUM RISORSE
########################################################
def get_numResources():
	
	#print '...in get_NumResources\n'
	field = "num_resources"
	count = 0


	# SOLR query
	fq = more_filters()  # filtra pkg in base alle organizzazioni dell'utente

	data_dict = {'fq': fq, 'rows': '3000'}
	if not c.user:
		data_dict = {'rows': '3000'} # non filtro per organizzazione

	# new

	diz = h.get_action('package_search', data_dict)
	
	if len(diz['results']) > 0:

		for pkg in diz['results']:
			if 'resources' in pkg:
				for res in pkg[ 'resources']:
					# se sloggato non conto risorse private
					if not (not c.user and res['resource_capacity'] == 'private'):
						count += 1


	"""
	data_dict = {'facet.field': [field], 'fq': fq}
	if not c.user:
		data_dict = {'facet.field': [field]} # non filtro per organizzazione


	diz = h.get_action('package_search', data_dict)

	
	#print diz
	if len(diz['facets']) > 0:
		diz = diz['facets'][field]
		#print diz
		for elem in diz.items():
			#print int(elem[0])
			#print int(elem[1])

			# ad esempio {'3':1} dice che esiste 1 pkg con 3 risorse

			count += int(elem[0]) * int(elem[1])
	"""
	
	return count







########################################################
# GET TAGS AND FREQUENCY	
########################################################	
def get_tags():	
	field= "tags"
	
	# SOLR query
	fq= more_filters() #filtra pkg in base alle organizzazioni dell'utente
	data_dict= {'facet.field':[field], 'fq':fq} 
	diz= h.get_action('package_search',data_dict )
	
	#print diz['facets'][field]
	if len(diz['facets']) == 0:
		return None
	else:
			
		diz= diz['facets'][field]
		count= len(diz) 
		diz= sorted(diz.items(), key=itemgetter(1), reverse=True)

		list=[]
		for elem in diz:
			target = {"text": elem[0], "size": elem[1]}
			list.append(target)
		
		if len(list)>=20: #prendo solo i 20 piu frequenti
			list=list[:20]
		
		return json.dumps(list)
	




########################################################
# GET APPLICATION AND FREQUENCY	
########################################################
def get_app():		
	field= "ico_applicazione_utilizza_banca_dati"
			
	# SOLR query
	fq= more_filters() #filtra pkg in base alle organizzazioni dell'utente
	data_dict= {'facet.field':[field], 'fq':fq} 
	diz= h.get_action('package_search',data_dict )

	if len(diz['facets']) == 0:
		return json.dumps({"labels":None, "data": None, "count": 0})

	else:
		diz= diz['facets'][field]
		count= len(diz) 
		diz= sorted(diz.items(), key=itemgetter(1), reverse=True)

		labels=[] 
		data=[]	
		for elem in diz:
			if elem[0] != "":
				labels.append(elem[0])			
				data.append(elem[1])
			else: #if the key is null don't count it
				count-=1

		return json.dumps({"labels":labels[:5], "data": data[:5], "count": count}) #only top 5


def get_app_full():		
	field= "ico_applicazione_utilizza_banca_dati"
			
	# SOLR query
	fq= more_filters() #filtra pkg in base alle organizzazioni dell'utente
	data_dict= {'facet.field':[field], 'fq':fq} 
	diz= h.get_action('package_search',data_dict )

	if len(diz['facets']) == 0:
		return json.dumps({"labels":None, "data": None, "count": 0})

	else:
		diz= diz['facets'][field]
		count= len(diz) 
		diz= sorted(diz.items(), key=itemgetter(1), reverse=True)

		labels=[] 
		data=[]	
		for elem in diz:
			if elem[0] != "":
				labels.append(elem[0])			
				data.append(elem[1])
			else: #if the key is null don't count it
				count-=1

		return json.dumps({"labels":labels[5:], "data": data[5:], "count": count}) # resto

 


########################################################
# GET SERVICES AND NUM DATASETS FOR EACH SERVICE
########################################################
def get_services():
	field= "publisher_name" 

	# SOLR query
	fq= more_filters() #filtra pkg in base alle organizzazioni dell'utente
	data_dict= {'facet.field':[field], 'fq':fq} 
	diz= h.get_action('package_search',data_dict )
	
	if len(diz['facets']) == 0:
		return json.dumps({"labels":None, "data": None, "count": 0})
	else:
		diz= diz['facets'][field]

		count= len(diz) 
		diz= sorted(diz.items(), key=itemgetter(1), reverse=True)

		labels=[] 
		data=[]	
		for elem in diz:
			if elem[0] != "":
				labels.append(elem[0])			
				data.append(elem[1])
			else: #if the key is null don't count it
				count-=1
		return json.dumps({"labels":labels[:5], "data": data[:5], "count": count}) #only top 5



def get_services_full():
	field= "publisher_name" 

	# SOLR query
	fq= more_filters() #filtra pkg in base alle organizzazioni dell'utente
	data_dict= {'facet.field':[field], 'fq':fq} 
	diz= h.get_action('package_search',data_dict )
	
	if len(diz['facets']) == 0:
		return json.dumps({"labels":None, "data": None, "count": 0})
	else:
		diz= diz['facets'][field]

		count= len(diz) 
		diz= sorted(diz.items(), key=itemgetter(1), reverse=True)

		labels=[] 
		data=[]	
		for elem in diz:
			if elem[0] != "":
				labels.append(elem[0])			
				data.append(elem[1])
			else: #if the key is null don't count it
				count-=1
		return json.dumps({"labels":labels[5:], "data": data[5:], "count": count}) 



