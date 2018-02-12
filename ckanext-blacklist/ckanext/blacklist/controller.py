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





class BlackListController(BaseController):
    """ 
    Controller per il plugin black_list
    """

    ########################
    def black_list(self, id):
	
	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}
        data_dict = {'id': id, 
		     'include_datasets':True,
		     'include_dataset_count': True }

	c.group_dict = get_action('organization_show')(context, data_dict)
	
	pacchetti= c.group_dict['packages']

	# vedo solo i privati ##########
	for elem in pacchetti:
		if elem[u'private']==False: 
			pacchetti.remove(elem)

	page= self._get_page_number(request.params) or 1

	c.current_page = int(page)
	c.prev_page = c.current_page -1	
	c.items_per_page =20 # da impostare a piacimento

	c.target = pacchetti
		
	c.datasets = c.target[c.prev_page * c.items_per_page : c.current_page * c.items_per_page]
	
	c.q = request.params.get('q', '')
	
	c.pkg_count = c.group_dict['package_count']


	c.page = h.Page(
                collection=c.target,
                page=self._get_page_number(request.params),
                #url=pager_url,
                item_count=c.pkg_count,
                items_per_page=c.items_per_page
            )

	c.page.items = c.target
	

        return render('blackList.html')	

    ########################
    def ready4open(self):
	
	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}
	
	# vedo solo i datest pubblici con almeno una risorsa
	q= 'capacity:public -num_resources:0'
	
	data_dict = {'q': q,
		     'rows': 1000}

	query = get_action('package_search')(context, data_dict)
	
	page= self._get_page_number(request.params) or 1
	
	c.target = query['results']

	c.current_page = int(page)
	c.prev_page = c.current_page -1	
	c.items_per_page =100 # da impostare a piacimento

	c.datasets = c.target[c.prev_page * c.items_per_page : c.current_page * c.items_per_page]

	c.q = request.params.get('q', '')
	
	c.pkg_count = len(c.target)

	c.page = h.Page(
                collection=c.target,
                page=self._get_page_number(request.params),
                #url=pager_url,
                item_count=c.pkg_count,
                items_per_page=c.items_per_page
            )

	c.page.items = c.target

        return render('ready4open.html')	

    ########################
    def visibility(self):
	
	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}

	# ZIP
	q = '-num_resources:0' # solo datasets con risorse
	fq = 'capacity:private' # solo privati
	data_dict = {
                'q': q,
                'fq': fq.strip(),
                #'facet.field': facets.keys(),
                'rows': 1000,
                #'start': (page - 1) * limit,
                #'sort': sort_by,
                #'extras': search_extras
        }

        query = get_action('package_search')(context, data_dict)
	
	
	# tengo solo risorse openData 
	open_format = ['ZIP', 'CSV', 'SHP', 'RDF', 'API/SPARQL']
	c.target = []
	for elem in query['results']:
		hasOPEN = False
		for ris in elem['resources']:
			#print ris['format']
			if ris['format'].upper() in open_format:
				hasOPEN = True
		if hasOPEN: 
			c.target.append(elem)
	return render('visibility.html')


    ########################
    def RDF(self):
	
	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}

	q = '-num_resources:0' # solo datasets con risorse
	fq = 'capacity:public'
	data_dict = {
                'q': q,
                #'fq': fq.strip(),
                #'facet.field': facets.keys(),
                'rows': 1000,
                #'start': (page - 1) * limit,
                #'sort': sort_by,
                #'extras': search_extras
        }

        query = get_action('package_search')(context, data_dict)
	
	# tengo solo RDF format 
	c.rdf = []
	for elem in query['results']:
		hasRDF = False
		for ris in elem['resources']:
			if ris['format'] == 'RDF':
				hasRDF = True
		if hasRDF: 
			c.rdf.append(elem)        
	return render('RDF.html')
