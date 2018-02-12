
from ckan.lib.celery_app import celery

@celery.task(name = "background.echofunction")
def echo( message ):
  print message






