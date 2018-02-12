

## Googleanalitics extension
googleanalytics.id = UA-107292309-1
googleanalytics.account = ckandemo
googleanalytics.username = fabio.stivanin@gmail.com
googleanalytics.password = <PSSWORD>>

INIT DB
paster initdb --config=/etc/ckan/default/development.ini


PER RACCOGLIERE STATISTICHE VA ESEGUITO OGNI TOT
(mettere file credentials.json dentro l'ext)
paster loadanalytics credentials.json --config=/etc/ckan/default/development.ini


MODULO GOOGLEAPI (se MANCA)
fare modifica al codice: 
	from googleapiclient.discovery import build
COMANDO
pip install --force-reinstall google-api-python-client


PER VEDERE STATISTICHE...
http://ckandemo.iconsulting.biz/analytics/dataset/top
da problemi 
  <xi:include href="layout.html" />
FUNZIONA SOLO SU CKAN 1.X ( ANDREBBE TOCCATO IL CODICE DELL'EXT)