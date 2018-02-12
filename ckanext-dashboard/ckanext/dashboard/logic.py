import json
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic.action.get as get
import requests
from sqlalchemy import create_engine
import unicodedata
from passlib.hash import pbkdf2_sha512

############################################################################################### METODI ACTION

@toolkit.side_effect_free
def get_user_from_header(context, data_dict):
	#print data_dict
	url = 'http://ckandemo.iconsulting.biz/user/login'
	response = requests.post(url)
	#print pbkdf2_sha512.decrypt('$pbkdf2-sha512$19000$TsnZe29tTYmRUgqhlBLiPA$JYP3qycT3w/jvccg21VZtwVas/MWcks7QS859f8PazfBGYFHHMwV.5S1q4szXdUzztBy/K.2dDwPQa8OlO4QXQ')
	response.headers['user'] = 'fsivanin'
	print type(response.headers) # TODO cambia '' in ""
	return response.headers
	# print 
