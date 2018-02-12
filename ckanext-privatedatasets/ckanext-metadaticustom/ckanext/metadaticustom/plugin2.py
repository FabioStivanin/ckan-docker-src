# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk

#################################################################################
def create_ico_vocabolario_GEMETs():
	user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
	context = {'user': user['name']}
	try:
		data = {'id': 'ico_vocabolario_GEMETs'}
		tk.get_action('vocabulary_show')(context, data)
	except tk.ObjectNotFound:
		data = {'name': 'ico_vocabolario_GEMETs'}
		vocab = tk.get_action('vocabulary_create')(context, data)
		
		for tag in (u'Assente',u'Abusivismo',u'Acqua',u'Aria',u'Autorizzazioni Paesaggistiche',u'Boschi-Foreste',u'Campi Elettromagnetici',u'Ciclopedonale',u'Corsi Acqua Pubblici',u'Dati Vettoriali PTCP',u'Edilizia',u'Geologia',u'Infrastrutture',u'Inquinamento Luminoso',u'Lavori Pubblici',u'Mobility Managment',u'Biodiversità',u'Oneri Urbanizzazione',u'Piano Territoriale Paesistico Regionale',u'Quadro Conoscitivo Territoriale',u'Rifiuti',u'Rischio Industriale',u'Rumore',u'Sicurezza Stradale',u'Sicurezza Territorio',u'Suolo',u'Sviluppo Sostenibile',u'TPL',u'Trasporti',u'Vincoli Archeologici',u'Vincoli Paesaggistici'):
			data = {'name': tag, 'vocabulary_id': vocab['id']}
			tk.get_action('tag_create')(context, data)

def ico_vocabolario_GEMETs():
	create_ico_vocabolario_GEMETs()
	try:
		tag_list = tk.get_action('tag_list')
		ico_vocabolario_GEMETs = tag_list(data_dict={'vocabulary_id': 'ico_vocabolario_GEMETs'})
		return ico_vocabolario_GEMETs
	except tk.ObjectNotFound:
		return None





#################################################################################
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
		
		
class MetadatiCustom(p.SingletonPlugin, tk.DefaultDatasetForm):
	p.implements(p.IDatasetForm)
	p.implements(p.IConfigurer)
	p.implements(p.ITemplateHelpers)
	
	def get_helpers(self):
		return {'ico_vocabolario_dato_certificatos':ico_vocabolario_dato_certificatos,'ico_vocabolario_attivitas':ico_vocabolario_attivitas,'ico_vocabolario_TDs':ico_vocabolario_TDs,'ico_vocabolario_Finanziamentis':ico_vocabolario_Finanziamentis,
		'ico_vocabolario_PPs':ico_vocabolario_PPs,'ico_vocabolario_LPs':ico_vocabolario_LPs,
		'ico_vocabolario_fonte_informaziones':ico_vocabolario_fonte_informaziones,'ico_vocabolario_EnCos':ico_vocabolario_EnCos,'ico_vocabolario_stTematica_ambientales': ico_vocabolario_stTematica_ambientales,
		'ico_vocabolario_Archivios':ico_vocabolario_Archivios,'ico_vocabolario_TAmbientales': ico_vocabolario_TAmbientales,'ico_vocabolario_modello_dpsirs': ico_vocabolario_modello_dpsirs,
		'ico_vocabolario_Elementis': ico_vocabolario_Elementis}
	
	
	def _modify_package_schema(self, schema):

		# Ripetere per ogni metadato nel template.xls
		
		schema.update({
			'ico_categoria_gemet': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_theme': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_categoria_eurovoc': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_url_eurovoc': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_sottocategoria_gemet': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_subtheme': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_sottocategoria_eurovoc': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_url_sottocategoria_eurovoc': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_tipologia_informazione': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		
		schema.update({
			'ico_nome_ente_responsabile': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_email_ente_responsabile': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_HomePage_Ente_Responsabile': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_tipo_ente_responsbile': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_nome_struttura_riferimento': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_rightsHolder': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_indirizzo_struttura_riferimento': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_recapito_telefonico_struttura_riferimento': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_email_struttura_riferimento': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_nome_creatore': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_creator': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_indirizzo_creatore': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_recapito_telefonico_creatore': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_email_creatore': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_referente': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_email_referente': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_recapito_telefonico_referente': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_lingua': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_language': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_area_geografica': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_url_area_geografica': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_livello_regionale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_url_livello_regionale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_livello_provinciale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_url_livello_provinciale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_livello_comunale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_url_livello_comunale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		
		schema.update({
			'ico_temporal_start': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_temporal_end': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_frequenza_aggiornamento': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_accuralPeriodicity': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		
		schema.update({
			'ico_isVersionOf': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_conformsTo': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_info_aggiuntive': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_richiesto_account': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_riferimenti_normativi': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_scala': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_applicazione_produce_banca_dati': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_applicazione_utilizza_banca_dati': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		schema.update({
			'ico_fornitore_applicazione': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		
		schema.update({
			'ico_metadatato_geoportale': [tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_extras')]
		})
		
		# Ripetere per ogni vocabolario
		
		schema.update({
			'ico_vocabolario_TAmbientale': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_TAmbientales')
			]
		})
		
		schema.update({
			'ico_vocabolario_Elementi': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_Elementis')
			]
		})
		
		schema.update({
			'ico_vocabolario_Archivio': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_Archivios')
			]
		})
		
		schema.update({
			'ico_vocabolario_stTematica_ambientale': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_stTematica_ambientales')
			]
		})
		
		schema.update({
			'ico_vocabolario_modello_dpsir': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_modello_dpsirs')
			]
		})
		
		schema.update({
			'ico_vocabolario_EnCo': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_EnCos')
			]
		})
		
		schema.update({
			'ico_vocabolario_fonte_informazione': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_fonte_informaziones')
			]
		})
		
		schema.update({
			'ico_vocabolario_LP': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_LPs')
			]
		})
		
		schema.update({
			'ico_vocabolario_PP': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_PPs')
			]
		})
		
		schema.update({
			'ico_vocabolario_Finanziamenti': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_Finanziamentis')
			]
		})
		
		schema.update({
			'ico_vocabolario_TD': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_TDs')
			]
		})
		
		schema.update({
			'ico_vocabolario_attivita': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_attivitas')
			]
		})
		
		schema.update({
			'ico_vocabolario_dato_certificato': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('ico_vocabolario_dato_certificatos')
			]
		})
		
		return schema

	def create_package_schema(self):
		schema = super(MetadatiCustom, self).create_package_schema()
		schema = self._modify_package_schema(schema)
		return schema

	def update_package_schema(self):
		schema = super(MetadatiCustom, self).update_package_schema()
		schema = self._modify_package_schema(schema)
		return schema


	def show_package_schema(self):
		schema = super(MetadatiCustom, self).show_package_schema()
		
		# Ripetere per ogni metadato nel template.xls
		
		schema.update({
			'ico_categoria_gemet': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_theme': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_categoria_eurovoc': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_url_eurovoc': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_sottocategoria_gemet': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_subtheme': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_sottocategoria_eurovoc': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_url_sottocategoria_eurovoc': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_tipologia_informazione': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_nome_ente_responsabile': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_email_ente_responsabile': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_HomePage_Ente_Responsabile': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_tipo_ente_responsbile': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_nome_struttura_riferimento': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_rightsHolder': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_indirizzo_struttura_riferimento': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_recapito_telefonico_struttura_riferimento': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_email_struttura_riferimento': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_nome_creatore': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_creator': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_indirizzo_creatore': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_recapito_telefonico_creatore': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_email_creatore': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_referente': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_email_referente': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_recapito_telefonico_referente': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_lingua': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_language': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_area_geografica': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_url_area_geografica': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_livello_regionale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_url_livello_regionale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_livello_provinciale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_url_livello_provinciale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_livello_comunale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_url_livello_comunale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_temporal_start': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_temporal_end': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_frequenza_aggiornamento': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_accuralPeriodicity': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_isVersionOf': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_conformsTo': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_info_aggiuntive': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_richiesto_account': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_riferimenti_normativi': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_scala': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_applicazione_produce_banca_dati': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_applicazione_utilizza_banca_dati': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		schema.update({
			'ico_fornitore_applicazione': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		
		schema.update({
			'ico_metadatato_geoportale': [tk.get_converter('convert_from_extras'),
				tk.get_validator('ignore_missing')]
		})
		
		
		# Ripetere per ogni vocabolario
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_TAmbientale': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_TAmbientales'),
				tk.get_validator('ignore_missing')]
		})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_Elementi': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_Elementis'),
				tk.get_validator('ignore_missing')]
		})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_Archivio': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_Archivios'),
				tk.get_validator('ignore_missing')]
		})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_stTematica_ambientale': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_stTematica_ambientales'),
				tk.get_validator('ignore_missing')]
		})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_modello_dpsir': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_modello_dpsirs'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_EnCo': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_EnCos'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_fonte_informazione': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_fonte_informaziones'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_LP': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_LPs'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_PP': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_PPs'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_Finanziamenti': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_Finanziamentis'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_TD': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_TDs'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_attivita': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_attivitas'),
				tk.get_validator('ignore_missing')]
			})
		
		schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
		schema.update({
			'ico_vocabolario_dato_certificato': [
				tk.get_converter('convert_from_tags')('ico_vocabolario_dato_certificatos'),
				tk.get_validator('ignore_missing')]
			})
		
		return schema
		
		
	def is_fallback(self):
		# Return True to register this plugin as the default handler for
		# package types not handled by any other IDatasetForm plugin.
		return True

	def package_types(self):
		# This plugin doesn't handle any special package types, it just
		# registers itself as the default (above).
		return []

	def update_config(self, config):
		# Add this plugin's templates dir to CKAN's extra_template_paths, so
		# that CKAN will use this plugin's custom templates.
		tk.add_template_directory(config, 'templates')
		
		
