import logging
import uuid
import requests

from pylons import session

import ckan.plugins as p
import ckan.lib.helpers as h
import ckan.model as model
import ckan.logic.schema as schema

t = p.toolkit
log = logging.getLogger(__name__)


def _no_permissions(context, msg):
	user = context['user']
	return {'success': False, 'msg': msg.format(user=user)}


@t.auth_sysadmins_check
def user_create(context, data_dict):
	msg = p.toolkit._('Users cannot be created.')
	return _no_permissions(context, msg)


@t.auth_sysadmins_check
def user_update(context, data_dict):
	msg = p.toolkit._('Users cannot be edited.')
	return _no_permissions(context, msg)


@t.auth_sysadmins_check
def user_reset(context, data_dict):
	msg = p.toolkit._('Users cannot reset passwords.')
	return _no_permissions(context, msg)


@t.auth_sysadmins_check
def request_reset(context, data_dict):
	msg = p.toolkit._('Users cannot reset passwords.')
	return _no_permissions(context, msg)

"""
ESTENSIONE PER AUTENTIZAZIONE TRAMITE IAM
sulla falsa riga dell'estensione ckanext-ldap (https://github.com/whythawk/ckanext-ldap)

NB: per abilitare aggiungere iam ai plugins nel file di config in etc/ckan/development.ini TODO

"""
class IamPlugin(p.SingletonPlugin):
	p.implements(p.IAuthenticator, inherit=True)
	p.implements(p.IAuthFunctions, inherit=True)
	p.implements(p.IConfigurer)
	#p.implements(p.IActions)
	
	# pagina di login diversa in iam/templates/user
	def update_config(self, config):
		t.add_template_directory(config, 'templates')
		

	# main login method
	def login(self):
		#url_iam = 'http://ckandemo.iconsulting.biz' # REQUEST TO IAM tipo GET/POST ? 
		#response = requests.get(url_iam) # IAM risponde con username nell'header
		#response.headers['user'] = 'fstivanin' # FIXME rimuovere in futuro
		#username = response.headers['user'] # FIXME leggo header, aggiungi in futuro

		username = t.request.headers.get('username')
		#username = t.request.POST.get('login') # FIXME rimuovere in futuro
		
		password = t.request.POST.get('password') #fstivanin FIXME rimuovi in futuro, non serve piu

		if username:
			userobj = model.User.get(username)
			if userobj: 
				session['iam_user'] = username
				session.save()

				h.redirect_to(controller='user', action='dashboard')
			else:
				h.flash_error('Inserisci un username valido in CKAN.')


	def logout(self):
		session['iam_user'] = None
		session.delete()

	def identify(self):

		iam_user = session.get('iam_user')
		#print iam_user
		c = t.c
		if iam_user:
			c.userobj = model.User.get(iam_user)
			c.user = iam_user

	def get_auth_functions(self):
		# we need to prevent some actions being authorized.
		return {
			'user_create': user_create,
			#'user_update': user_update,
			'user_reset': user_reset,
			'request_reset': request_reset
		}
