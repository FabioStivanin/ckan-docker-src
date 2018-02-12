import ckan.logic as logic
import ckan.authz as authz
import ckan.logic.auth as logic_auth
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic.action.get as get
from ckan.logic import get_action
import ckan.model as model
import requests
from sqlalchemy import create_engine
from ckan.lib.base import BaseController, render
import unicodedata
from ckan.common import OrderedDict, _, json, request, c, g, response
import time

import os
import uuid
import shutil
import gc
import zipfile
import shapefile
from json import dumps
import urllib2
from subprocess import call
from os.path import splitext

# API di tipo GET
@toolkit.side_effect_free 
def get_geojson_from_shp(context,data_dict):

	url = data_dict['url'] 
	path1 = url[:3]
	path2 = url[3:6]
	filename = url[6:]
	storage_path = '/var/lib/ckan/default/resources'# simile a ckan.storage_path	
	input_file = os.path.join(storage_path, path1 , path2, filename)

	unique_id = str(uuid.uuid1()).replace(" ","")
	directory = './'+ unique_id
	os.makedirs(directory)
	zip_ref = zipfile.ZipFile(input_file, 'r')
	zip_ref.extractall(directory)
	zip_ref.close()

	onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) ]
	for file in onlyfiles:
		file_name, extension = splitext(file)
		# cerco .shp file
		if extension == '.shp':
			shape_file = file

	#chiama il comando docker...
	command = "docker run -v /usr/lib/ckan/default/src/ckanext-dashboard/"+ unique_id
	command += ":/shapes geographica/gdal2 ogr2ogr "
	command += "-simplify 100 "
	command += "-overwrite -f GeoJSON -t_srs EPSG:4326 "
	command += "/shapes/shape.geojson /shapes/"+ shape_file
	call(command, shell=True)

	json = open(os.path.join("/usr/lib/ckan/default/src/ckanext-dashboard/"+ unique_id, "shape.geojson"), "r")
	gc.collect()
	content =""
	with json as f:
		for line in f:
			content += line
	#rimuovo cartella
	shutil.rmtree("/usr/lib/ckan/default/src/ckanext-dashboard/"+ unique_id)

	return content.decode('utf-8', 'ignore')




@toolkit.side_effect_free 
def resource_upload_datastore(context,data_dict):

		    print data_dict
		    id_risorsa= data_dict['id']
		    #print id_risorsa
		    url = id_risorsa
		    import unicodedata
		    import csv
		    url= unicodedata.normalize('NFKD', url).encode('ascii', 'ignore')  # str url del csv
		    path1 = url[:3]
		    path2 = url[3:6]
		    filename = url[6:]

		    #storage_path = '/opt/ckan/default/storage/resources'
		    storage_path = '/var/lib/ckan/default/resources' # ckandemo
		    input_file = os.path.join(storage_path, path1, path2, filename)
		    
		    #print input_file + "\n\n"

		    csvfile = open(input_file, 'rU')
		
		    reader = csv.DictReader(csvfile)

		    # Created a list and adds the rows of the csv to the list
		    json_list = []
		    
		    i= 0
		    for row in reader:
			for elem in row:
				row[elem] = str(row[elem])
				#print str(row[elem])

			json_list.append(row)
			print row
			i = i+1
			if i==2: break
			
		    upload_host = 'datacatalog.regione.emilia-romagna.it/catalogCTA'
		    upload_api = '05320953-abbc-4217-a0c3-4175f627828d'

		    #host = '10.5.16.82:5000' #ckandemo
    		    #idUtente = '6d0fccec-859a-4b99-995c-a026b0d5e1f3' 

                    requesta = urllib2.Request('https://' + upload_host + '/api/action/datastore_create')

                    requesta.add_header('Authorization', upload_api)
		    
		    id_risorsa2 = data_dict['id2'] 

		    print id_risorsa

		    print id_risorsa2

		    store_dict = {
				  'force': True, 
				  'resource_id': id_risorsa2,
				  'records': json_list
					}

		    data_string = urllib2.quote(json.dumps(store_dict))
		    print data_string

                    # Make the HTTP request.
                    response = urllib2.urlopen(requesta, data_string.encode('utf8')).read()

                    response_dict = json.loads(response.decode('utf-8'))

                    # Controlla if TRUE
                    assert response_dict['success'] is True
		    
		    print response_dict['success']
		    """
	            
		    #json_list = json.dumps(json.loads(json_list))
		    #json_list.replace("'",'"')
		    #json_list = json.loads(json_list)
		    print json_list
		    print  type(json_list)
		    
		    
		    
		    store_dict = {"force": True, 
				  "resource_id": id_risorsa,
				  "records": json_list}

		    print 'before datastore create\n'
		    try:
		    	query = get_action('datastore_create')(context, store_dict) # DATASTORE CREATE
		    except:
			print '\nERRORE in datastore create! =('
		    """
		    print "end package.py/datastore\n\n"
		    ##################################################################################

















