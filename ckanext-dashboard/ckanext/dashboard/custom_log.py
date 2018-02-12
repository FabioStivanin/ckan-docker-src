import logging
from ckan.common import c
from ckan.lib.helpers import get_action
import ckan.model as model
import requests

import pylons
from pylons import request

class CustomFormatter(logging.Formatter):
	def __init__(self, default):
		self.default = default

	def format(self, record):

		user=""
		try:
			if pylons.c.user:
				user= "USER="+str(pylons.c.user)
			else: 
				user= "USER=NotLogged"
		except:
			pass

		""" IP DI CHI FA LA RICHIESTA?
		ip = request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"])
		print ip
		"""
		record.user = user
		#record.msg = '[%s] %s PID=%d [%s] %s' % (record.levelname, user, record.process, record.name, record.msg)

		return self.default.format(record)

def factory(fmt, datefmt):
	default = logging.Formatter(fmt, datefmt)
	return CustomFormatter(default)