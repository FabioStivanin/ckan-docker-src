import ckan.logic as logic
import ckan.authz as authz
import ckan.logic.auth as logic_auth
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import ckan.logic.action.get as get
from ckan.logic import get_action
import ckan.lib.helpers as h
import ckan.model as model
import requests
from sqlalchemy import create_engine
from ckan.lib.base import BaseController, render
import unicodedata
from ckan.common import OrderedDict, _, json, request, c, g, response 
import time
import datetime
import ckan.lib.plugins as lib_plugins
import ckan.lib.dictization.model_save as model_save

get_action = logic.get_action



def blacklist_package_update(context, data_dict):

    model = context['model']
    user = context['user']
    name_or_id = data_dict.get("id") or data_dict['name']

    pkg = model.Package.get(name_or_id)
    if pkg is None:
        raise NotFound(_('Package was not found.'))
    context["package"] = pkg
    data_dict["id"] = pkg.id
    data_dict['type'] = pkg.type

    # get the schema
    package_plugin = lib_plugins.lookup_package_plugin(pkg.type)		

    if 'schema' in context:
        schema = context['schema']
    else:
        schema = package_plugin.update_package_schema()

	schema.update({
		'black_list': [toolkit.get_validator('ignore_missing'),
				toolkit.get_converter('convert_to_extras')]
		})


    if 'api_version' not in context:
        # check_data_dict() is deprecated. If the package_plugin has a
        # check_data_dict() we'll call it, if it doesn't have the method we'll
        # do nothing.
        check_data_dict = getattr(package_plugin, 'check_data_dict', None)
        if check_data_dict:
            try:
                package_plugin.check_data_dict(data_dict, schema)
            except TypeError:
                # Old plugins do not support passing the schema so we need
                # to ensure they still work.
                package_plugin.check_data_dict(data_dict)
    
    data, errors = lib_plugins.plugin_validate(
        package_plugin, context, data_dict, schema, 'package_update')

    
        
    rev = model.repo.new_revision()
    rev.author = user
    if 'message' in context:
        rev.message = context['message']
    else:
        rev.message = _(u'REST API: Update object %s') % data.get("name")

    #avoid revisioning by updating directly
    model.Session.query(model.Package).filter_by(id=pkg.id).update(
        {"metadata_modified": datetime.datetime.utcnow()})
    model.Session.refresh(pkg)

    pkg = model_save.package_dict_save(data, context)

    context_org_update = context.copy()
    context_org_update['ignore_auth'] = True
    context_org_update['defer_commit'] = True
    get_action('package_owner_org_update')(context_org_update,
                                            {'id': pkg.id,
                                             'organization_id': pkg.owner_org})

    # Needed to let extensions know the new resources ids
    model.Session.flush()
    if data.get('resources'):
        for index, resource in enumerate(data['resources']):
            resource['id'] = pkg.resources[index].id

    for item in plugins.PluginImplementations(plugins.IPackageController):
        item.edit(pkg)

        item.after_update(context, data)

    # Create default views for resources if necessary
    if data.get('resources'):
        logic.get_action('package_create_default_resource_views')(
            {'model': context['model'], 'user': context['user'],
             'ignore_auth': True},
            {'package': data})

    if not context.get('defer_commit'):
        model.repo.commit()

    return_id_only = context.get('return_id_only', False)

    # Make sure that a user provided schema is not used on package_show
    context.pop('schema', None)

    # we could update the dataset so we should still be able to read it.
    context['ignore_auth'] = True
    output = data_dict['id'] if return_id_only \
            else get_action('package_show')(context, {'id': data_dict['id']})

    return output


def rdf_package_update(context, data_dict):

    model = context['model']
    user = context['user']
    name_or_id = data_dict.get("id") or data_dict['name']

    pkg = model.Package.get(name_or_id)
    if pkg is None:
        raise NotFound(_('Package was not found.'))
    context["package"] = pkg
    data_dict["id"] = pkg.id
    data_dict['type'] = pkg.type

    # get the schema
    package_plugin = lib_plugins.lookup_package_plugin(pkg.type)		

    if 'schema' in context:
        schema = context['schema']
    else:
        schema = package_plugin.update_package_schema()

	 
	schema.update({
			'load_rdf_job_identifier': [toolkit.get_validator('ignore_missing'),
				toolkit.get_converter('convert_to_extras')]
		})
	schema.update({
			'load_rdf_job_start': [toolkit.get_validator('ignore_missing'),
				toolkit.get_converter('convert_to_extras')]
		})

    if 'api_version' not in context:
        # check_data_dict() is deprecated. If the package_plugin has a
        # check_data_dict() we'll call it, if it doesn't have the method we'll
        # do nothing.
        check_data_dict = getattr(package_plugin, 'check_data_dict', None)
        if check_data_dict:
            try:
                package_plugin.check_data_dict(data_dict, schema)
            except TypeError:
                # Old plugins do not support passing the schema so we need
                # to ensure they still work.
                package_plugin.check_data_dict(data_dict)
    
    data, errors = lib_plugins.plugin_validate(
        package_plugin, context, data_dict, schema, 'package_update')

    
        
    rev = model.repo.new_revision()
    rev.author = user
    if 'message' in context:
        rev.message = context['message']
    else:
        rev.message = _(u'REST API: Update object %s') % data.get("name")

    #avoid revisioning by updating directly
    model.Session.query(model.Package).filter_by(id=pkg.id).update(
        {"metadata_modified": datetime.datetime.utcnow()})
    model.Session.refresh(pkg)

    pkg = model_save.package_dict_save(data, context)

    context_org_update = context.copy()
    context_org_update['ignore_auth'] = True
    context_org_update['defer_commit'] = True
    get_action('package_owner_org_update')(context_org_update,
                                            {'id': pkg.id,
                                             'organization_id': pkg.owner_org})

    # Needed to let extensions know the new resources ids
    model.Session.flush()
    if data.get('resources'):
        for index, resource in enumerate(data['resources']):
            resource['id'] = pkg.resources[index].id

    for item in plugins.PluginImplementations(plugins.IPackageController):
        item.edit(pkg)

        item.after_update(context, data)

    # Create default views for resources if necessary
    if data.get('resources'):
        logic.get_action('package_create_default_resource_views')(
            {'model': context['model'], 'user': context['user'],
             'ignore_auth': True},
            {'package': data})

    if not context.get('defer_commit'):
        model.repo.commit()

    return_id_only = context.get('return_id_only', False)

    # Make sure that a user provided schema is not used on package_show
    context.pop('schema', None)

    # we could update the dataset so we should still be able to read it.
    context['ignore_auth'] = True
    output = data_dict['id'] if return_id_only \
            else get_action('package_show')(context, {'id': data_dict['id']})

    return output










############################################
def black_list_update(context, checked):
	#print "BLACK_LIST"
	# checked is the dict with the names of pkgs we want to update and the users involved
	ids = checked['dataset'].split(",")
	
	user_to_black = checked['lista_update'].split(",")

	if "null" not in user_to_black:
		user_to_black = [x.encode('UTF8') for x in user_to_black ] #to string
	else:
		user_to_black=[]


	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}
	count=1
	for name in ids:
			name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
			print name
			print count
			count+=1

			# OLD VERSION OF THE PKG
			q= 'name:'+name
			query = get_action('package_search')(context, {'q': q})
			print "query"
			data_dict= query['results'][0]# unicode dict
			if (u'blacklist' in data_dict.keys()): 
				print "in"
				bl= data_dict[u'black_list'].replace("{", "").replace("}", "").split(",")
				if (u'opendata_member' in bl) :
					user_to_black.append('opendata_member')
			print "\nSearched and"	
			# update pkg only if necessary	###############
			if (u'black_list' not in data_dict.keys() or data_dict[u'black_list'].replace("{", "").replace("}", "").split(",") != user_to_black ): 	        				
				data_dict[u'black_list']= user_to_black			
				blacklist_package_update(context, data_dict) 
				print " updated.\n"	
				

	
	return 'OK'


############################################
def update_opendata(context, checked):
	#print "BLACK_LIST"
	# checked is the dict with the names of pkgs we want to update and the users involved
	ids = checked['dataset'].split(",")
	flag= (checked['flag'] == 'make_true')
	#print ids
	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}

	for name in ids:
			name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
			#print name

			# OLD VERSION OF THE PKG
			q= 'name:'+name
			query = get_action('package_search')(context, {'q': q})
			data_dict= query['results'][0]# unicode dict
			#print "\nSearched and"	
			if u'black_list' not in data_dict.keys(): #FIX rimuovi in futuro inutile perche' set in creazione
				old_list=[u'opendata_member']
			elif data_dict[u'black_list']!="{}" :
				old_list = data_dict[u'black_list'].replace("{", "").replace("}", "").split(",") 
			else:
				old_list=[]		
			
			if flag: # TO OPEN
				if u'opendata_member' not in old_list:
					#print old_list
					return "Nessuna modifica necessaria"	
				old_list.remove('opendata_member')	
				

			else: #back to NOT OPEN rimuovi in futuro
				if u'opendata_member' not in old_list:
					old_list.append('opendata_member')
				

			data_dict[u'black_list'] = old_list
			blacklist_package_update(context, data_dict) 
			#print " updated.\n"					

	
	return 'OK'


############################################
def update_if_loadRDF(context,checked):
	# checked is the dict with the names of pkgs we want to change metadata job rdf
	ids = checked['dataset'].split(", ")

	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}

	for name in ids:	
		name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')

		# OLD VERSION OF THE PKG
		q= 'name:'+name
		query = get_action('package_search')(context, {'q': q})
		data_dict= query['results'][0]# unicode dict
		#print "\nSearched and"	
	
		# PKG METADATA UPDATED
		if u'load_rdf_job_start' not in data_dict.keys(): 
			data_dict[u'load_rdf_job_start']= time.strftime("%d %b %Y %H:%M:%S")					
			rdf_package_update(context, data_dict) 
			#print " metadata updated at time: "+time.strftime("%c")+"\n"	
	
	return "OK"



############################################
def custom_update_to_public(context,checked):
	print "in"
	# checked is the dict with the names of pkgs we want to set private
	ids = checked['dataset'].split(",")

	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}

	for name in ids:
		name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
		print name

		# OLD VERSION OF THE PKG
		q= 'name:'+name
		query = get_action('package_search')(context, {'q': q})

		data_dict= query['results'][0]# unicode dict
		#print "\nSearched and"	
	
		# PKG UPDATED TO PUBLIC
		# NB --> POTREI AVER PROBLEMI DI UPDTE PKG A CAUSA DI CAT. GEMET ERRATE ##############
		data_dict[u'private']= False 					
		query = get_action('package_update')(context, data_dict) 
		#print " updated.\n"	
	
	return "OK"





 
