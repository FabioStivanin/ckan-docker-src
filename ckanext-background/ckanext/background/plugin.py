import ckan.plugins as p
from ckan.common import session
import ckan.plugins.toolkit as toolkit

import twitter
#https://pypi.python.org/pypi/python-twitter/

import time
import datetime


class BackgroundPlugin(p.SingletonPlugin):
    '''
    Automatically send tweets when a dataset is updated or created.
    '''
    p.implements(p.IConfigurer)
    p.implements(p.IPackageController, inherit = True)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'background')

    # IPackageController
    def after_update(self, context, pkg_dict):

	# Variables that contains the user credentials to access Twitter API 

	# TODO leggi da file di configurazione

	ACCESS_TOKEN = '961158953496399872-AYYq8nd0uGRqkT3edxPsx9sERAPPahF'
	ACCESS_SECRET = '015cQUa7KXxMEzTnYrSQMncNC6qeiDCIMMLVW3rqb7zsW'
	CONSUMER_KEY = 'ZsN2Udo3jqmQQLUzYFYWMReNb'
	CONSUMER_SECRET = 'FAgLnwcWhZpsZ25ukkStUM3QzCGboivfMgn6QQt4CRdVn2whEl'

	api = twitter.Api(consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	access_token_key=ACCESS_TOKEN,
	access_token_secret=ACCESS_SECRET)

	#print api.VerifyCredentials()
	date = datetime.date.today().strftime("%d/%m/%Y")
	time = datetime.datetime.now().strftime("%H:%M:%S")
	
	# TESTO DEL MESSAGGIO
	m= "Catalogo aggiornato!\n"
	m = m + "Dataset: "+ pkg_dict['name'] + "\n"
	if 'notes' in pkg_dict:
		m = m + "Descrizione: "+ pkg_dict['notes'] + "\n"
	m = m + "\n\n "+ date +" ore " + time

	# API CHE TWITTA
	status = api.PostUpdate(m)
	#print status.text





