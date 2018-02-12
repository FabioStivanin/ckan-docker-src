import ckan.logic as logic
import ckan.authz as authz
import ckan.logic.auth as logic_auth
import ckan.logic.action.get as get
from ckan.logic import get_action
import ckan.model as model
import requests
import unicodedata
from sqlalchemy import create_engine
from ckan.lib.base import BaseController, render
from ckan.common import OrderedDict, _, json, request, c, g, response

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.blacklist.logic import black_list_update, update_opendata, custom_update_to_public, update_if_loadRDF, blacklist_package_update, rdf_package_update
from ckanext.blacklist.util import update_all







class BlacklistPlugin(plugins.SingletonPlugin):
	plugins.implements(plugins.IActions)
	plugins.implements(plugins.IConfigurer)
	plugins.implements(plugins.IRoutes)




	# IActions ########################################

	def get_actions(self):
		# Registers the custom API method defined above
		return {
			'black_list_update': black_list_update,
			'update_opendata': update_opendata,
			'custom_update_to_public' : custom_update_to_public,
			'update_if_loadRDF' : update_if_loadRDF,
			'blacklist_package_update' : blacklist_package_update,
			'rdf_package_update': rdf_package_update,
			'update_all':update_all
			
		}


	# IConfigurer ######################################

	def update_config(self, config_):
		#toolkit.add_template_directory(config_, 'templates')
		#toolkit.add_public_directory(config_, 'public')
		toolkit.add_resource('fanstatic', 'blacklist')


	# IRoutes ######################################
	
	def before_map(self, route_map):
		import routes.mapper
		with routes.mapper.SubMapper(route_map, controller='ckanext.blacklist.controller:BlackListController') as m:
			m.connect('black', '/blackList/{id}', action='black_list', ckan_icon='lock')
		with routes.mapper.SubMapper(route_map, controller='ckanext.blacklist.controller:BlackListController') as m:
			m.connect('ready4open', '/ready4open', action='ready4open', ckan_icon='star')
		with routes.mapper.SubMapper(route_map, controller='ckanext.blacklist.controller:BlackListController') as m:
			m.connect('visibility', '/visibility', action='visibility', ckan_icon='eye-open')
		with routes.mapper.SubMapper(route_map, controller='ckanext.blacklist.controller:BlackListController') as m:
			m.connect('RDF', '/RDF', action='RDF' , ckan_icon='arrow-up')
		with routes.mapper.SubMapper(route_map, controller='ckanext.blacklist.controller:BlackListController') as m:
			m.connect('opendata', '/opendata', action='visibility')
		return route_map


	def after_map(self, route_map):
		return route_map






