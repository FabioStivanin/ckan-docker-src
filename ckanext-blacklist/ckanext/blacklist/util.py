import ckan.logic as logic
import ckan.authz as authz
import ckan.logic.auth as logic_auth
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
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


######################################
def purge_all(context, data_dict):
		print "PURGING..."
		user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
		context = {'user': user['name'] }
		
		q=''
		res_dict= logic.get_action('package_search')(context, {'q':q, 'rows':100})
		
		
		for pkg in res_dict['results']:
			pkg_id=unicodedata.normalize('NFKD', pkg[u'id']).encode('ascii','ignore')
			#print pkg_id
			logic.get_action('dataset_purge')(context, {'id':pkg_id})
		print str(len(res_dict['results'])) +' datasets purged'
		return "OK"	

######################################
def update_all(context, data_dict):
		print "UPDATING..."
		user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
		context = {'user': user['name'] }
		
		q='organization:ambiente'
		
		data_dict= {'q':q, 
			    'rows':100}
		res_dict= logic.get_action('package_search')(context, {'q':q, 'rows':1000})
		
		checked={}
		str=""
		strani=0
		for pkg in res_dict['results']:
			pkg_name=pkg[u'name'] #unicodedata.normalize('NFKD', pkg[u'name']).encode('ascii','ignore')
			#print pkg_id
			if pkg_name[0]!="-": #FIXME
				str +=pkg_name+","
			else: 
				strani+=1
		str=str[:-1] # tolgo ultima virgola
		checked['dataset']=str
		checked['lista_update']="opendata_member"
		logic.get_action('black_list_update')(context, checked)
		print ' datasets updated'
		#print strani
		return "OK"	
