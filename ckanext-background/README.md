# ESTENSIONE CHE PUBBLICA SU TWITTER L'AGGIORNAMENTO DI UN DATASET NUOVO O ESISTENTE

# INSTALLAZIONE

1) creare un account twitter, ad esempio
https://twitter.com/test_catalogCTA

2) Prendere le chiavi di autenticazione registrando l'applicazione su
https://apps.twitter.com/

	ACCESS_TOKEN = '961158953496399872-AYYq8nd0uGRqkT3edxPsx9sERAPPahF'
	ACCESS_SECRET = '015cQUa7KXxMEzTnYrSQMncNC6qeiDCIMMLVW3rqb7zsW'
	CONSUMER_KEY = 'ZsN2Udo3jqmQQLUzYFYWMReNb'
	CONSUMER_SECRET = 'FAgLnwcWhZpsZ25ukkStUM3QzCGboivfMgn6QQt4CRdVn2whEl'

Attenzione a dare i permessi corretti di lettura, scrittura.
esempio: https://apps.twitter.com/app/14775709/show

3) Abilitare l'applicazione a twitter
https://twitter.com/settings/applications

4) modificare le chiavi nel file plugin.py con quelle del punto (2)

5) eseguire dentro ckanext-background 
python setup.py develop

(NB! necessaria libreria python-twitter)
pip install -r requirements.txt 


