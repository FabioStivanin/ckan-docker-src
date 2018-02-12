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
from ckan.lib.base import BaseController, render


from pylons.controllers.util import redirect_to, redirect
from routes import url_for

# ALTRI CONTROLLERS

# pagina con iframe


class LocationController(BaseController):
	def location(self):
		return render('geoviewer.html')


class StatisticheController(BaseController):
	def statistiche(self):

		#redirect('/dashboard')
		f = open("statistiche.txt","w")
		
		c.organo=[]
		organo = h.get_action('organization_list', {'all_fields':True, 'include_dataset_count':True})
		for ooo in organo:
			c.organo.append(ooo['display_name'] + ": " + str(ooo['package_count'])) 


		group_diz={}
		group_list= h.get_action('group_list', {'all_fields':True, 'include_dataset_count':True})
		org_list= h.get_action('organization_list', {})
		c.stat=[]

		for group in group_list:
			c.statistiche=""
			g= unicodedata.normalize('NFKD', group['display_name']).encode('ascii', 'ignore')
			f.write('\nGRUPPO: '+g.upper()+ ' --> ' + str(group['package_count'])+' dataset:\n')
			g= unicodedata.normalize('NFKD', group['name']).encode('ascii', 'ignore')

			c.statistiche = c.statistiche + '\nGRUPPO: '+g.upper()+ ' --> ' + str(group['package_count'])+' dataset:\n'		
			
			q= '+groups:"'+g+'"'
			data_dict = {'q': q,  'rows':2000,  }
			diz = h.get_action('package_search', data_dict)
			results= diz['results']
			
			privati = 0
			pubblici =0
			for pkg in diz['results']:
				if pkg['private']:
					privati+=1
				else:
					pubblici +=1


			c.statistiche = c.statistiche + ' priv '+ str(privati)+ ' , pub '+ str(pubblici)
			
			if diz['results']:
				for org in org_list:
					o= unicodedata.normalize('NFKD', org).encode('ascii', 'ignore')
					f.write('> org = '+o)
					c.statistiche = c.statistiche + '> org = > org =  '+o.upper()
					q= '+groups:"'+g+'"'+' +organization:"'+o+'"'
					#fq='capacity:"public"'
					data_dict = {'q': q,  'rows':2000,  }
					diz = h.get_action('package_search', data_dict)
					results= diz['results']
					c.statistiche = c.statistiche + ' ('+ str(len(diz['results']))+' DS TOT) > org =\nRIS: \n'
					wms=0
					shp=0
					altro=0
					priv_wms=0
					pub_wms=0
					priv_shp=0
					pub_shp=0
					priv_altro=0
					pub_altro=0
					senza_risorse = 0
					privati = 0
					for pkg in diz['results']:
						if pkg['private']:
							privati+=1
						if pkg['num_resources']==0:
							senza_risorse +=1

						for res in pkg[u'resources']:
							if res[u'format'].upper()==u'WMS':
								wms+=1
								if res[u'resource_capacity']==u'public' and pkg[u'private']==False:
									pub_wms+=1
								else:
									priv_wms+=1
							elif res[u'format'].upper()==u'SHP':
								shp+=1
								if res[u'resource_capacity']==u'public' and pkg[u'private']==False:
									pub_shp+=1
								else:
									priv_shp+=1
							else:
								altro+=1
								if res[u'resource_capacity']==u'public' and pkg[u'private']==False:
									pub_altro+=1
								else:
									priv_altro+=1
								
					tot= wms+ shp+ altro
					tot_priv = priv_wms+ priv_shp + priv_altro
					tot_pub = pub_wms+ pub_shp + pub_altro
					f.write('\nwms: '+str(   wms)+' ( privati '+str(   priv_wms)+', pubblici '+str(   pub_wms) +')')
					c.statistiche = c.statistiche + '\nwms: '+str(   wms)+' ( privati '+str(   priv_wms)+', pubblici '+str(   pub_wms) +')'
					f.write('\nshp: '+str(   shp)+' ( privati '+str(   priv_shp)+', pubblici '+str(   pub_shp) +')')
					c.statistiche = c.statistiche + '\nshp: '+str(   shp)+' ( privati '+str(   priv_shp)+', pubblici '+str(   pub_shp) +')'
					f.write('\naltre: '+str(   altro)+ ' ( privati '+str(   priv_altro)+', pubblici '+str(   pub_altro) +')')
					c.statistiche = c.statistiche + '\naltre: '+str(   altro)+ ' ( privati '+str(   priv_altro)+', pubblici '+str(   pub_altro) +')'
					f.write('\ntotali: '+str(tot)+' ( privati '+str(tot_priv)+', pubblici '+str(tot_pub) +')\n\n')
					c.statistiche = c.statistiche +'\ntotali: '+str(tot)+' ( privati '+str(tot_priv)+', pubblici '+str(tot_pub) +')\n\n'
					if senza_risorse>0 :
						c.statistiche = c.statistiche + '\n; Senza RIS:'+ str(senza_risorse)
			c.stat.append(c.statistiche)

		f.close()

		return render('statistiche.html')
