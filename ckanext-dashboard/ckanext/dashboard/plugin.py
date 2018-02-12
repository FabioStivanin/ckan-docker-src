import ckan.logic as logic
import ckan.authz as authz
import ckan.logic.auth as logic_auth
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic.action.get as get
from ckan.logic import get_action
import ckan.model as model
import requests
import json
import unicodedata
from sqlalchemy import create_engine
from ckan.lib.base import BaseController, render
import unicodedata
from ckan.lib.helpers import url_for_static_or_external

from ckanext.dashboard.helper import ( get_numDatasets, get_numGroups, get_numResources, get_tags
				     , get_app, get_app_full, get_services, get_services_full )

from ckanext.dashboard.util import get_geojson_from_shp, resource_upload_datastore
from ckan.common import c
import ckan.lib.helpers as h

from pylons.controllers.util import redirect_to, redirect
from routes import url_for

from ckanext.dashboard.uploader import CustomResourceUpload
from ckan.lib.uploader import Upload

def user_update(context, data_dict):
	user = context['user']
	# FIXME: We shouldn't have to do a try ... except here, validation should
	# have ensured that the data_dict contains a valid user id before we get to
	# authorization.
	try:
		user_obj = logic_auth.get_user_object(context, data_dict)
	except logic.NotFound:
		return {'success': False, 'msg': _('User not found')}

	# If the user has a valid reset_key in the db, and that same reset key
	# has been posted in the data_dict, we allow the user to update
	# her account without using her password or API key.
	if user_obj.reset_key and 'reset_key' in data_dict:
		if user_obj.reset_key == data_dict['reset_key']:
			return {'success': True}

	if not user:
		return {'success': False, 'msg': _('Have to be logged in to edit user')}

	if user == user_obj.name:
	#print "ok"
	# Allow users to update their own user accounts.
		return {'success': True}
	else:
		# Don't allow users to update other users' accounts.
		#print "not autorized"
		return {'success': False,'msg': _('User %s not authorized to edit user %s') % (user, user_obj.id)}



def custom_redirect():
	redirect(url_for(controller='user', action='dashboard'), code=303)


####################################################### 
# MAIN PLUGIN CLASS
#######################################################
class DashboardPlugin(plugins.SingletonPlugin):
	#plugins.implements(plugins.IConfigurable)
	plugins.implements(plugins.interfaces.IActions)
	plugins.implements(plugins.interfaces.IFacets)
	plugins.implements(plugins.IConfigurer)
	plugins.implements(plugins.ITemplateHelpers)
	plugins.implements(plugins.IRoutes)
	plugins.implements(plugins.interfaces.IAuthFunctions)
	plugins.implements(plugins.interfaces.IUploader, inherit=True)
	#plugins.implements(plugins.IPackageController, inherit=True)
	

	# IPackage INTERFACE
	######################################################
	def before_search(self, search_params):
		if 'rows' in search_params:
			search_params['extras']['old_rows'] = search_params['rows']
			search_params['rows'] = 4000
		if 'start' in search_params:
			search_params['extras']['old_start'] = search_params['start']
			search_params['start'] = 0
		return search_params
		

	def after_search(self, search_results, search_params):

		
		query = search_results
		data_dict= search_params

		count = search_results['count']
		fq = data_dict['fq'][0]
		try:
			ex_start = data_dict['extras']['old_start'] 
			ex_rows = data_dict['extras']['old_rows']
		except:
			pass

		special_format =[]
		lista_format= fq.split('+')
		l=[]
		for form in lista_format: 
			x = form.split(':')
			if x[0] == u'res_format':
				special_format.append(x[1].replace('"',''))


		for package in query['results']:
			# get the package object
			package_dict = package
			# use data in search index if there
			if package_dict:

				# the package_dict still needs translating when being viewed
				#package_dict = json.loads(package_dict)

				organizzazione = package_dict['organization']['id']
				# fast modifica risorse private

				# pkg pubblico con risorse
				dic_format = {} #serve dopo

				if package_dict['private'] == False and package_dict['num_resources'] > 0:
					risorse_visibili = []
					for risorsa in package_dict['resources']:
						formato = risorsa['format']
						if not formato in dic_format.keys():
							 dic_format[formato]=0
						if 'resource_capacity' in risorsa.keys():

							# NB non faccio vedere risorse private a opendata e ai non membri
							if not (risorsa['resource_capacity'] == 'private' and (not h.user_in_org_or_group(organizzazione) or user == 'opendata_member')):

								#print 'Tengo ' + risorsa['name']+ '.' + formato
								risorse_visibili.append(risorsa)
								dic_format[formato]+=1


							else:  # risorsa rimossa
								dic_format[formato]-=1
								#print 'Rimuovo ' + risorsa['name']+ '.' + formato # RESOURCE NON VISIBILE DA PKG SEARCH\n"
						else:
							risorse_visibili.append(risorsa)
							dic_format[formato]+=1


					if 'res_format' in query['facets'].keys():
						for formato in dic_format:
							if dic_format[formato]<0 :
								query['facets']['res_format'][formato] -= 1
								if query['facets']['res_format'][formato] == 0:
										del(query['facets']['res_format'][formato])

					if 'num_resources' in query['facets'].keys() and package_dict['num_resources'] != len(risorse_visibili):

						# ad esempio {'3':1} dice che esiste 1 pkg con 3 risorse
						
						query.facets['num_resources'][ str(package_dict['num_resources'])]-=1
						if query['facets']['num_resources'][ str(package_dict['num_resources'])] == 0:
							del(query['facets']['num_resources'][ str(package_dict['num_resources'])])

						if len(risorse_visibili)>0:
							query.facets['num_resources'][ str(len(risorse_visibili))]+=1

					package_dict['num_resources'] = len(risorse_visibili)
					package_dict['resources'] = risorse_visibili



				hide = False
				# fast controllo forse superfluo su organizzazione utente per loggati
				organizzazione = package_dict['organization']['id']
				# se privato e non sei membro non lo vedi
				if package_dict['private'] == True and not h.user_in_org_or_group(organizzazione):
					hide = True
				else:
					# fast modifiche piu recenti BLACKLIST autorizzazione livello utente
					# se sloggato ed esiste metadato controllo BL
					# se loggato controllo BL
					if ('black_list' in package_dict.keys()):

						lista_black = unicodedata.normalize('NFKD', package_dict[u'black_list']).encode('ascii', 'ignore')
						lista_black = lista_black[1:-1].split(",")

						if package_dict['private'] == False:  # se pubblico

							# unico caso particolare OM in BL
							if (user == 'opendata_member' and 'opendata_member' in lista_black):
								hide = True

						else:  # se privato
							# controllo se user in BL (a prescindere i privati nascosti a OM)
							if (user == 'opendata_member' or user in lista_black):
								hide = True

				for format in dic_format:
					if (format in special_format and dic_format[format] <0):
						hide = True
					else:
						hide = False
				if hide:
					count = count - 1
				else:
					results.append(package_dict)

			else:
				log.error('No package_dict is coming from solr for package '
						  'id %s', package['id'])

		if count == 0:
			facets = {}
		else:
			facets = query.facets

		# fast modifica autorizzazione livello utente

		search_results = {
			'count': count,
			'facets': facets,
			'results': results[ex_start:ex_start + ex_rows],
			'sort': data_dict['sort']
			}

		return search_results







	# IConfigurable INTERFACE
	######################################################
	def configure(self, config):
		return
		"""
		print config
		CONFIG = u'''
		[loggers]
		keys=root
		[handlers]
		keys=console
		[handler_console]
		class=logging.StreamHandler
		args=(sys.stderr,)
		formatter=custom
		[formatters]
		keys=custom
		[logger_root]
		level=DEBUG
		handlers=console
		[formatter_custom]
		format=%(asctime)s %(message)s
		datefmt=%X
		class=ckanext.dashboard.custom_log.factory

		'''

		cfg = StringIO(CONFIG)
		logging.config.fileConfig(cfg)
		"""

	# iAction INTERFACE
	######################################################
	def get_actions(self):
		# Registers the custom API method defined above
		return {
			'get_geojson_from_shp': get_geojson_from_shp,
			'resource_upload_datastore': resource_upload_datastore
		}



	# IAuth INTERFACE
	#######################################################
	def get_auth_functions(self):
		return {'user_update':user_update}


	
	# IFacets INTERFACE
	# Filters on the left size of dataset page
	# Modify and return the facets_dict for dataset, organization and group's page
	#######################################################
	def dataset_facets(self, facets_dict, package_type):

		# add new facets (string)
		facets_dict['publisher_name'] =toolkit._('Strutture di Riferimento')

		####>> N.B. for vocabularies add vocab_!!!
		facets_dict['vocab_ico_categoria_gemet'] =toolkit._('Tema GEMET')
		facets_dict['vocab_ico_vocabolario_TAmbientales'] = toolkit._('Tematiche Ambientali')
		return facets_dict


	def organization_facets(self, facets_dict, organization_type, package_type):
		facets_dict['publisher_name'] =toolkit._('Strutture di Riferimento')

		facets_dict['vocab_ico_categoria_gemet'] = toolkit._('Tema GEMET')
		facets_dict['vocab_ico_vocabolario_TAmbientales'] = toolkit._('Tematiche Ambientali')
		return facets_dict


	def group_facets(self, facets_dict, group_type, package_type):
		facets_dict['publisher_name'] =toolkit._('Strutture di Riferimento')

		facets_dict['vocab_ico_categoria_gemet'] =toolkit._('Tema GEMET')
		facets_dict['vocab_ico_vocabolario_TAmbientales'] = toolkit._('Tematiche Ambientali')
		return facets_dict


	
	# IConfigurer INTERFACE
	#######################################################
	def update_config(self, config_):
		#toolkit.add_template_directory(config_, 'templates') #templates path
		#toolkit.add_public_directory(config_, 'public')
		toolkit.add_resource('fanstatic', 'dash')  #where to add css and refer to



	# ITemplateHelpers INTERFACE
	# methods defined in ckanext.dashboard.helper
	#######################################################

	def get_helpers(self):
		# register our helper function
		return {'get_numDatasets': get_numDatasets,
			'get_numGroups': get_numGroups,
			'get_numResources': get_numResources,
			'get_tags': get_tags,
			'get_app': get_app,
			'get_app_full': get_app_full,
			'get_services': get_services,
			'get_services_full': get_services_full,
			'custom_redirect': custom_redirect,
			'url_statico' : url_for_static_or_external
			}




	# IRoutes INTERFACE
	################################
	def before_map(self, route_map):
		
		import routes.mapper

		with routes.mapper.SubMapper(route_map, controller='ckanext.dashboard.controller:LocationController') as m:
			m.connect('geoviewer', '/geoviewer', action='location')

		with routes.mapper.SubMapper(route_map, controller='ckanext.dashboard.controller:StatisticheController') as m:
			m.connect('statistiche', '/statistiche', action='statistiche')

		return route_map

	def after_map(self, route_map):
		return route_map



	# IUploader INTERFACE
	#####################

	def get_resource_uploader(self, data_dict):
		return CustomResourceUpload(data_dict)


	def get_uploader(self, upload_to, old_filename):
		return Upload(upload_to, old_filename)








