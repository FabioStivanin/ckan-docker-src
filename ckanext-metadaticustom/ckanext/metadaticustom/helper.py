# encoding: utf-8
import os
import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.model as model
import ckan.logic.validators as validators
from ckan.common import _, c

######### metodo per vocab black_list da form
def vocab_black_list():
	lista_utenti=[]
	context = {'model': model, 'session': model.Session, 'user': c.user or c.author}
					   
	org_list= tk.get_action('organization_list')(context, {})

	
	for org_name in org_list:
		members = tk.get_action('member_list')(context, {'id':org_name})
		
		for member in members:
			user_id, oggetto, ruolo = member
			if oggetto == 'user' and ruolo != 'Amministratore':
				 user = tk.get_action('user_show')(context, {'id': user_id})
				 user_name = user['name']
				 if user_name not in lista_utenti:
					lista_utenti.append(user_name) 				
	lista_utenti.sort()	
	#print [x.encode('UTF8') for x in lista_utenti]	#from unicode to str
	return lista_utenti


######################## 
# tema DCAT
########################
def create_ico_vocabolario_themes():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'theme'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'theme'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		#vocab = tk.get_action('vocabulary_update')(context, data)
		
		vocabolario=[]	
		vocabolario.append(unicode("N.D.", "utf-8")) # must be unicode

		for tag in vocabolario:
		   #if tag not in tk.get_action('tag_list')(data_dict={'vocabulary_id': 'theme'}):
			if ","  in tag: 
				tag= tag.replace(",", "-")
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)
	 

def ico_vocabolario_themes():
	create_ico_vocabolario_themes()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_themes = tag_list(data_dict={'vocabulary_id': 'theme'})
		return ico_vocabolario_themes
	except tk.ObjectNotFound:
		return None




######### new metadata
def create_vocabolario_applicativi_infrastrutturalis():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'vocabolario_applicativi_infrastrutturalis'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'vocabolario_applicativi_infrastrutturalis'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (): # TODO ADD LIST
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def vocabolario_applicativi_infrastrutturalis():
	create_vocabolario_applicativi_infrastrutturalis()
	try:
		tag_list = tk.get_action('tag_list')
		vocabolario_applicativi_infrastrutturalis = tag_list(data_dict={'vocabulary_id': 'vocabolario_applicativi_infrastrutturalis'})
		return vocabolario_applicativi_infrastrutturalis
	except tk.ObjectNotFound:
		return None

######### new metadata
def create_vocabolario_applicazioni_collegates():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'vocabolario_applicazioni_collegates'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'vocabolario_applicazioni_collegates'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (): # TODO ADD LIST
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def vocabolario_applicazioni_collegates():
	create_vocabolario_applicazioni_collegates()
	try:
		tag_list = tk.get_action('tag_list')
		vocabolario_applicazioni_collegates = tag_list(data_dict={'vocabulary_id': 'vocabolario_applicazioni_collegates'})
		return vocabolario_applicazioni_collegates
	except tk.ObjectNotFound:
		return None






######################## 
# categorie GEMET 
########################
def create_ico_vocabolario_GEMETs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_categoria_gemet'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_categoria_gemet'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		#vocab = tk.get_action('vocabulary_update')(context, data)

		
		path= os.getcwd() 
		file= open(path+"/ckanext/dashboard/public/gemet-groups.txt","r")
		txt=file.read()
		file.close()
		list= txt.split(";")
		vocabolario=[]	
		for item in list:
			item=item.split(":")
			vocabolario.append(unicode(item[1], "utf-8")) # must be unicode

		for tag in vocabolario:
		    	#if tag not in tk.get_action('tag_list')(data_dict={'vocabulary_id': 'ico_categoria_gemet'}):

			#if ","  in tag: 
			#	tag= tag.replace(",", "-")
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)
		#print "end create vocab"
	 

def ico_vocabolario_GEMETs():
	create_ico_vocabolario_GEMETs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_GEMETs = tag_list(data_dict={'vocabulary_id': 'ico_categoria_gemet'})
		return ico_vocabolario_GEMETs
	except tk.ObjectNotFound:
		return None



######################## 
# sottoCategorie GEMET 
########################
def create_ico_vocabolario_sottoGEMETs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_sottocategoria_gemet'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		#data = {'name': 'ico_sottocategoria_gemet'}
		vocab = tk.get_action('vocabulary_update')(context, data)
		#vocab = tk.get_action('vocabulary_create')(context, data)

		path= os.getcwd() 
		file= open(path+"/ckanext/dashboard/public/sottogemet.txt","r")
		######## ATTENZIONE MODIFICATO I NOMI PERCHE' NON ACCETTAVA APOSTROFI E PARENTESI 
		txt=file.read()
		file.close()
		list= txt.split(";")	
		vocabolario=[]	
		for item in list:
				item=item.split(":")
				vocabolario.append(unicode(item[1], "utf-8"))
		for tag in vocabolario:
			if tag not in tk.get_action('tag_list')(data_dict={'vocabulary_id': 'ico_sottocategoria_gemet'}):
				data = {'name': tag, 'vocabulary_id': vocab['id']}
				tk.get_action('tag_create')(context, data)
				#print data
		#print "end create vocab"
	 

def ico_vocabolario_sottoGEMETs():
	create_ico_vocabolario_sottoGEMETs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_sottoGEMETs = tag_list(data_dict={'vocabulary_id': 'ico_sottocategoria_gemet'})
		return ico_vocabolario_sottoGEMETs
	except tk.ObjectNotFound:
		return None










def create_ico_vocabolario_modello_dpsirs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_modello_dpsirs'}
		tk.get_action('vocabulary_show')(context, data)
		
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_modello_dpsirs'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Pressione', u'Stato', u'Risposta'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_modello_dpsirs():
	create_ico_vocabolario_modello_dpsirs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_modello_dpsirs = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_modello_dpsirs'})
		return ico_vocabolario_modello_dpsirs
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_TAmbientales():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_TAmbientales'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_TAmbientales'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Abusivismo',u'Acqua',u'Aria',u'Autorizzazioni Paesaggistiche',u'Boschi-Foreste',u'Campi Elettromagnetici',u'Ciclopedonale',u'Corsi Acqua Pubblici',u'Dati Vettoriali PTCP',u'Edilizia',u'Geologia',u'Infrastrutture',u'Inquinamento Luminoso',u'Lavori Pubblici',u'Mobility Managment',u'Biodiversità',u'Oneri Urbanizzazione',u'Piano Territoriale Paesistico Regionale',u'Quadro Conoscitivo Territoriale',u'Rifiuti',u'Rischio Industriale',u'Rumore',u'Sicurezza Stradale',u'Sicurezza Territorio',u'Suolo',u'Sviluppo Sostenibile',u'TPL',u'Trasporti',u'Vincoli Archeologici',u'Vincoli Paesaggistici'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_TAmbientales():
	create_ico_vocabolario_TAmbientales()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_TAmbientales = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_TAmbientales'})
		return ico_vocabolario_TAmbientales
	except tk.ObjectNotFound:
		return None


def create_ico_vocabolario_Elementis():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_Elementis'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_Elementis'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Terra',u'Aria',u'Acqua'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_Elementis():
	create_ico_vocabolario_Elementis()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_Elementis = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_Elementis'})
		return ico_vocabolario_Elementis
	except tk.ObjectNotFound:
		return None


def create_ico_vocabolario_Archivios():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_Archivios'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_Archivios'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Archiviato',u'Non Archiviato'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_Archivios():
	create_ico_vocabolario_Archivios()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_Archivios = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_Archivios'})
		return ico_vocabolario_Archivios
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_stTematica_ambientales():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_stTematica_ambientales'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_stTematica_ambientales'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Analisi Costi-Benefici',u'Attuazione legislazione ambientale',u'Fattori incidenti sugli elementi ambientali',u'Misure legislative',u'Misure politiche',u'Salute e sicurezza',u'Stato elementi ambientali'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_stTematica_ambientales():
	create_ico_vocabolario_stTematica_ambientales()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_stTematica_ambientales = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_stTematica_ambientales'})
		return ico_vocabolario_stTematica_ambientales
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_EnCos():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_EnCos'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_EnCos'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Ministero Ambiente',u'Agenzia Demanio',u'Agenzia Regionale Protezione Civile',u'Agenzie TPL',u'AIPO',u'Anas',u'ARNI',u'ARPA',u'ASPI',u'ATO',u'AUSL',u'Autorita Bacino',u'Attivita Vigilanza Lavori Pubblici',u'Comuni',u'Consorzio Bonifica',u'Enti Locali',u'Enti Parco',u'Enti Territoriali',u'Esercenti',u'Fer',u'Gestori Autostradali',u'Servizio Gestione Rifiuti Urbani',u'INAIL',u'INPS',u'MB',u'MIBACT',u'Ministeri',u'Prefettura',u'Province',u'Regione Emilia-Romagna',u'Servizio Difesa SUolo-Costa-Bonifica',u'Seta',u'Sovrintendenze',u'StackHolders',u'Tper',u'Trenitalia'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_EnCos():
	create_ico_vocabolario_EnCos()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_EnCos = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_EnCos'})
		return ico_vocabolario_EnCos
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_fonte_informaziones():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_fonte_informaziones'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_fonte_informaziones'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'SATAP',u'CISA',u'Centro Padane',u'Autostrade Italia SPA',u'A22 Autostrada Brennero',u'ARPA',u'Autorita Bacino',u'Proponenti',u'Province',u'Regione Emilia-Romagna',u'RFI',u'Servizio Geologico',u'Consorzi Bonifica Regionali'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_fonte_informaziones():
	create_ico_vocabolario_fonte_informaziones()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_fonte_informaziones = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_fonte_informaziones'})
		return ico_vocabolario_fonte_informaziones
	except tk.ObjectNotFound:
		return None


def create_ico_vocabolario_LPs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_LPs'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_LPs'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Pubblicato',u'Non Pubblicato',u'In parte pubblicato',u'Pubblicabile',u'Non Pubblicabile',u'Uso Interno'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_LPs():
	create_ico_vocabolario_LPs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_LPs = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_LPs'})
		return ico_vocabolario_LPs
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_PPs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_PPs'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_PPs'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Geoportale',u'Sito FER',u'Opendata',u'Portale RER'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_PPs():
	create_ico_vocabolario_PPs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_PPs = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_PPs'})
		return ico_vocabolario_PPs
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_Finanziamentis():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_Finanziamentis'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_Finanziamentis'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Europeo',u'Statale',u'Regionale',u'Assente'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_Finanziamentis():
	create_ico_vocabolario_Finanziamentis()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_Finanziamentis = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_Finanziamentis'})
		return ico_vocabolario_Finanziamentis
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_TDs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_TDs'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_TDs'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Dato Grezzo',u'Indicatore',u'Dato Destrutturato',u'Mappa'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_TDs():
	create_ico_vocabolario_TDs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_TDs = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_TDs'})
		return ico_vocabolario_TDs
	except tk.ObjectNotFound:
		return None

def create_ico_vocabolario_attivitas():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_attivitas'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_attivitas'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Monitoraggio',u'Permessi',u'Pianificazione',u'Non Richiesto'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_attivitas():
	create_ico_vocabolario_attivitas()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_attivitas = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_attivitas'})
		return ico_vocabolario_attivitas
	except tk.ObjectNotFound:
		return None
		
def create_ico_vocabolario_dato_certificatos():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_dato_certificatos'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_dato_certificatos'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Non Certificato',u'Certificato'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_dato_certificatos():
	create_ico_vocabolario_dato_certificatos()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_dato_certificatos = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_dato_certificatos'})
		return ico_vocabolario_dato_certificatos
	except tk.ObjectNotFound:
		return None		
