# encoding: utf-8
import re
import os
import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.model as model
import ckan.logic.validators as validators
from ckan.common import _
from ckanext.metadaticustom.helper import (	ico_vocabolario_dato_certificatos, ico_vocabolario_attivitas, ico_vocabolario_TDs, ico_vocabolario_Finanziamentis,
											ico_vocabolario_PPs, ico_vocabolario_LPs, ico_vocabolario_fonte_informaziones, ico_vocabolario_EnCos, ico_vocabolario_stTematica_ambientales,
											ico_vocabolario_Archivios, ico_vocabolario_TAmbientales, ico_vocabolario_modello_dpsirs, ico_vocabolario_Elementis,
											ico_vocabolario_GEMETs,  ico_vocabolario_sottoGEMETs, ico_vocabolario_themes,
											vocab_black_list,
											vocabolario_applicativi_infrastrutturalis, vocabolario_applicazioni_collegates
											)

from ckanext.metadaticustom.converter import (gemet_converter, converter_from_ico_to_dcat)


def set_value(default_value):

	def callable(key, data, errors, context):

		data[key] = default_value

	return callable


# MAIN PLUGIN CLASS
class MetadatiCustom(p.SingletonPlugin, tk.DefaultDatasetForm):
	p.implements(p.IDatasetForm)
	p.implements(p.IConfigurer)
	p.implements(p.ITemplateHelpers)
	p.implements(p.IValidators)

	def get_helpers(self):
		return {'ico_vocabolario_dato_certificatos': ico_vocabolario_dato_certificatos, 'ico_vocabolario_attivitas': ico_vocabolario_attivitas, 'ico_vocabolario_TDs': ico_vocabolario_TDs, 'ico_vocabolario_Finanziamentis': ico_vocabolario_Finanziamentis,
				'ico_vocabolario_PPs': ico_vocabolario_PPs, 'ico_vocabolario_LPs': ico_vocabolario_LPs,
				'ico_vocabolario_fonte_informaziones': ico_vocabolario_fonte_informaziones, 'ico_vocabolario_EnCos': ico_vocabolario_EnCos, 'ico_vocabolario_stTematica_ambientales': ico_vocabolario_stTematica_ambientales,
				'ico_vocabolario_Archivios': ico_vocabolario_Archivios, 'ico_vocabolario_TAmbientales': ico_vocabolario_TAmbientales, 'ico_vocabolario_modello_dpsirs': ico_vocabolario_modello_dpsirs,
				'ico_vocabolario_Elementis': ico_vocabolario_Elementis,
				'ico_vocabolario_GEMETs': ico_vocabolario_GEMETs, 'ico_vocabolario_sottoGEMETs': ico_vocabolario_sottoGEMETs, 'ico_vocabolario_themes': ico_vocabolario_themes,
				'vocab_black_list': vocab_black_list,
				'vocabolario_applicativi_infrastrutturalis': vocabolario_applicativi_infrastrutturalis, 'vocabolario_applicazioni_collegates': vocabolario_applicazioni_collegates
				}

	def get_validators(self):
		return{'gemet_converter': gemet_converter,
			   'converter_from_ico_to_dcat': converter_from_ico_to_dcat,
			   'set_value': set_value
			   }

	#################################
	# METADATI IN CREATE
	#################################
	def _create_package_schema(self, schema):

		# BLACK_LIST -> change authorization user level for single pkgs
		schema.update({
			'black_list': [tk.get_validator('set_value')('opendata_member'),
						   tk.get_converter('convert_to_extras')]
		})

		# Metadati per pagina OpenData
		schema.update({
			'load_rdf_job_identifier': [tk.get_validator('ignore_missing'),
										tk.get_converter('convert_to_extras')]
		})
		schema.update({
			'load_rdf_job_start': [tk.get_validator('ignore_missing'),
								   tk.get_converter('convert_to_extras')]
		})

		# Ripetere per ogni metadato nel template.xls

		extra_metadata = ['language',
						  'metadata_manager_rer_identifier',
						  'data_di_sincronizzazione',
						  'maintainer_identifier',
						  'ico_categoria_eurovoc', 'ico_sottocategoria_eurovoc',
						  'ico_tipologia_informazione',
						  'holder_identifier', 'holder_name',
						  'ico_rightsHolder',
						  'ico_email_ente_responsabile', 'ico_HomePage_Ente_Responsabile', 'ico_tipo_ente_responsbile',
						  'publisher_identifier', 'publisher_name',
						  'ico_indirizzo_struttura_riferimento', 'ico_recapito_telefonico_struttura_riferimento', 'ico_email_struttura_riferimento',
						  'ico_referente', 'ico_email_referente', 'ico_recapito_telefonico_referente',
						  'temporal_start', 'temporal_end',
						  'ico_area_geografica', 'ico_url_area_geografica', 'ico_livello_regionale', 'ico_livello_provinciale', 'ico_livello_comunale',
						  'frequency', 'ico_accuralPeriodicity',
						  'is_version_of', 'conforms_to',
						  'ico_info_aggiuntive', 'ico_metadatato_geoportale',
						  'ico_fornitore_applicazione', 'ico_applicazione_utilizza_banca_dati', 'ico_applicazione_produce_banca_dati',
						  'ico_scala', 'ico_richiesto_account', 'ico_riferimenti_normativi',
						  'identifier', 'tipo_dataset',
						  'data_di_creazione_dato', 'data_di_aggiornamento_dato','data_di_pubblicazione_dato', 'url_thumbnail_esposizione'
						  ]

		for metadato in extra_metadata:
			schema.update({
				metadato: [tk.get_validator('ignore_missing'),
						   tk.get_converter('convert_to_extras')]
			})

		# Vecchi metadati da trasporre nei nuovi nomi #########################

		dcat_metadata = ['ico_nome_ente_responsabile', 'ico_nome_struttura_riferimento', 'ico_lingua',
						 'ico_temporal_start', 'ico_temporal_end', 'ico_frequenza_aggiornamento',
						 'ico_isVersionOf', 'ico_conformsTo'
						 ]

		for metadato in dcat_metadata:
			schema.update({
				metadato: [tk.get_validator('ignore_missing'),
						   tk.get_converter('converter_from_ico_to_dcat')]
			})

		# Ripetere per ogni vocabolario #######################################

		vocab_metadata = ['ico_vocabolario_TAmbientale', 'ico_vocabolario_Elementi', 'ico_vocabolario_Archivio', 'ico_vocabolario_stTematica_ambientale',
						  'ico_vocabolario_modello_dpsir', 'ico_vocabolario_EnCo', 'ico_vocabolario_fonte_informazione', 'ico_vocabolario_LP', 'ico_vocabolario_PP',
						  'ico_vocabolario_Finanziamenti', 'ico_vocabolario_TD', 'ico_vocabolario_attivita', 'ico_vocabolario_dato_certificato',
						  'vocabolario_applicativi_infrastrutturali', 'vocabolario_applicazioni_collegate'
						  ]

		for metadato in vocab_metadata:

			schema.update({
				metadato: [
					tk.get_validator('ignore_missing'),
					tk.get_converter('convert_to_tags')(metadato + "s")]
			})

		# Altri metadati... ###################################################

		schema.update({
			'ico_categoria_gemet': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('gemet_converter')('ico_categoria_gemet')
			]
		})

		schema.update({
			'ico_sottocategoria_gemet': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('gemet_converter')('ico_sottocategoria_gemet')
			]
		})

		schema.update({
			'theme': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('theme')
			]
		})

		# CUSTOM LICENSE TO RESOURCE
		schema['resources'].update({
			'resource_license': [tk.get_validator('ignore_missing')]
		})
		# Risorse pubbliche/private
		schema['resources'].update({
			'resource_capacity': [tk.get_validator('default')('public')]
		})

		return schema

	def create_package_schema(self):
		schema = super(MetadatiCustom, self).create_package_schema()
		schema = self._create_package_schema(schema)
		return schema

	#################################
	# METADATI IN UPDATE
	#################################
	def _update_package_schema(self, schema):

		# Ripetere per ogni metadato nel template.xls

		extra_metadata = ['language',
						  'metadata_manager_rer_identifier',
						  'data_di_sincronizzazione',
						  'maintainer_identifier',
						  'ico_categoria_eurovoc', 'ico_sottocategoria_eurovoc',
						  'ico_tipologia_informazione',
						  'holder_identifier', 'holder_name',
						  'ico_rightsHolder',
						  'ico_email_ente_responsabile', 'ico_HomePage_Ente_Responsabile', 'ico_tipo_ente_responsbile',
						  'publisher_identifier', 'publisher_name',
						  'ico_indirizzo_struttura_riferimento', 'ico_recapito_telefonico_struttura_riferimento', 'ico_email_struttura_riferimento',
						  'ico_referente', 'ico_email_referente', 'ico_recapito_telefonico_referente',
						  'temporal_start', 'temporal_end',
						  'ico_area_geografica', 'ico_url_area_geografica', 'ico_livello_regionale', 'ico_livello_provinciale', 'ico_livello_comunale',
						  'frequency', 'ico_accuralPeriodicity',
						  'is_version_of', 'conforms_to',
						  'ico_info_aggiuntive', 'ico_metadatato_geoportale',
						  'ico_fornitore_applicazione', 'ico_applicazione_utilizza_banca_dati', 'ico_applicazione_produce_banca_dati',
						  'ico_scala', 'ico_richiesto_account', 'ico_riferimenti_normativi',
						  'identifier', 'tipo_dataset',
						  'data_di_creazione_dato', 'data_di_aggiornamento_dato','data_di_pubblicazione_dato', 'url_thumbnail_esposizione'
						  ]

		for metadato in extra_metadata:
			schema.update({
				metadato: [tk.get_validator('ignore_missing'),
						   tk.get_converter('convert_to_extras')]
			})

		# Vecchi metadati da trasporre nei nuovi nomi #########################

		dcat_metadata = ['ico_nome_ente_responsabile', 'ico_nome_struttura_riferimento', 'ico_lingua',
						 'ico_temporal_start', 'ico_temporal_end', 'ico_frequenza_aggiornamento',
						 'ico_isVersionOf', 'ico_conformsTo'
						 ]

		for metadato in dcat_metadata:
			schema.update({
				metadato: [tk.get_validator('ignore_missing'),
						   tk.get_converter('converter_from_ico_to_dcat')]
			})

		# Ripetere per ogni vocabolario #######################################

		vocab_metadata = ['ico_vocabolario_TAmbientale', 'ico_vocabolario_Elementi', 'ico_vocabolario_Archivio', 'ico_vocabolario_stTematica_ambientale',
						  'ico_vocabolario_modello_dpsir', 'ico_vocabolario_EnCo', 'ico_vocabolario_fonte_informazione', 'ico_vocabolario_LP', 'ico_vocabolario_PP',
						  'ico_vocabolario_Finanziamenti', 'ico_vocabolario_TD', 'ico_vocabolario_attivita', 'ico_vocabolario_dato_certificato',
						  'vocabolario_applicativi_infrastrutturali', 'vocabolario_applicazioni_collegate'
						  ]

		for metadato in vocab_metadata:

			schema.update({
				metadato: [
					tk.get_validator('ignore_missing'),
					tk.get_converter('convert_to_tags')(metadato + "s")]
			})

		# Altri metadati... ###################################################

		schema.update({
			'ico_categoria_gemet': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('gemet_converter')('ico_categoria_gemet')
			]
		})

		schema.update({
			'ico_sottocategoria_gemet': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('gemet_converter')('ico_sottocategoria_gemet')
			]
		})

		schema.update({
			'theme': [
				tk.get_validator('ignore_missing'),
				tk.get_converter('convert_to_tags')('theme')
			]
		})

		# CUSTOM LICENSE TO RESOURCE
		schema['resources'].update({
			'resource_license': [tk.get_validator('ignore_missing')]
		})

		# Risorse pubbliche/private
		schema['resources'].update({
			'resource_capacity': [tk.get_validator('default')('public')]
		})

		return schema

	def update_package_schema(self):
		schema = super(MetadatiCustom, self).update_package_schema()
		schema = self._update_package_schema(schema)
		return schema

	##############################
	# PKG SHOW
	##############################
	def show_package_schema(self):
		schema = super(MetadatiCustom, self).show_package_schema()

		extra_metadata = ['language',
						  'metadata_manager_rer_identifier',
						  'data_di_sincronizzazione',
						  'maintainer_identifier',
						  'ico_categoria_eurovoc', 'ico_sottocategoria_eurovoc',
						  'ico_tipologia_informazione',
						  'holder_identifier', 'holder_name',
						  'ico_rightsHolder',
						  'ico_email_ente_responsabile', 'ico_HomePage_Ente_Responsabile', 'ico_tipo_ente_responsbile',
						  'publisher_identifier', 'publisher_name',
						  'ico_indirizzo_struttura_riferimento', 'ico_recapito_telefonico_struttura_riferimento', 'ico_email_struttura_riferimento',
						  'ico_referente', 'ico_email_referente', 'ico_recapito_telefonico_referente',
						  'temporal_start', 'temporal_end',
						  'ico_area_geografica', 'ico_url_area_geografica', 'ico_livello_regionale', 'ico_livello_provinciale', 'ico_livello_comunale',
						  'frequency', 'ico_accuralPeriodicity',
						  'is_version_of', 'conforms_to',
						  'ico_info_aggiuntive', 'ico_metadatato_geoportale',
						  'ico_fornitore_applicazione', 'ico_applicazione_utilizza_banca_dati', 'ico_applicazione_produce_banca_dati',
						  'ico_scala', 'ico_richiesto_account', 'ico_riferimenti_normativi',
						  'identifier', 'tipo_dataset',
						  'data_di_creazione_dato', 'data_di_aggiornamento_dato','data_di_pubblicazione_dato', 'url_thumbnail_esposizione'
						  ]

		for metadato in extra_metadata:
			schema.update({
				metadato: [tk.get_converter('convert_from_extras'),
						   tk.get_validator('ignore_missing')]
			})

		# Vecchi metadati da trasporre nei nuovi nomi #########################

		dcat_metadata = ['ico_nome_ente_responsabile', 'ico_nome_struttura_riferimento', 'ico_lingua',
						 'ico_temporal_start', 'ico_temporal_end', 'ico_frequenza_aggiornamento',
						 'ico_isVersionOf', 'ico_conformsTo'
						 ]

		for metadato in dcat_metadata:
			schema.update({
				metadato: [tk.get_converter('convert_from_extras'),
						   tk.get_validator('ignore_missing')]
			})

		# Ripetere per ogni vocabolario ##############################

		vocab_metadata = ['ico_vocabolario_TAmbientale', 'ico_vocabolario_Elementi', 'ico_vocabolario_Archivio', 'ico_vocabolario_stTematica_ambientale',
						  'ico_vocabolario_modello_dpsir', 'ico_vocabolario_EnCo', 'ico_vocabolario_fonte_informazione', 'ico_vocabolario_LP', 'ico_vocabolario_PP',
						  'ico_vocabolario_Finanziamenti', 'ico_vocabolario_TD', 'ico_vocabolario_attivita', 'ico_vocabolario_dato_certificato',
						  'vocabolario_applicativi_infrastrutturali', 'vocabolario_applicazioni_collegate'
						  ]

		for metadato in vocab_metadata:
			schema['tags']['__extras'].append(
				tk.get_converter('free_tags_only'))
			schema.update({
				metadato: [
					tk.get_converter('convert_from_tags')(metadato + "s"),
					tk.get_validator('ignore_missing')]
			})

		schema['tags']['__extras'].append(
			tk.get_converter('free_tags_only'))  # ICO CAT GEMET
		schema.update({
			'ico_categoria_gemet': [
				tk.get_converter('convert_from_tags')('ico_categoria_gemet'),
				tk.get_validator('ignore_missing')]
		})

		schema['tags']['__extras'].append(
			tk.get_converter('free_tags_only'))  # ICO SOTTO GEMET
		schema.update({
			'ico_sottocategoria_gemet': [
				tk.get_converter('convert_from_tags')(
					'ico_sottocategoria_gemet'),
				tk.get_validator('ignore_missing')]
		})

		schema['tags']['__extras'].append(
			tk.get_converter('free_tags_only'))  # DCAT THEME
		schema.update({
			'theme': [
				tk.get_converter('convert_from_tags')('theme'),
				tk.get_validator('ignore_missing')]
		})

		# altri metadati
		# BLACK_LIST -> change authorization user level for single pkgs
		schema.update({
			'black_list': [tk.get_converter('convert_from_extras'),
						   tk.get_validator('ignore_missing')]
		})

		# Metadati per pagina OpenData
		schema.update({
			'load_rdf_job_identifier': [tk.get_converter('convert_from_extras'),
										tk.get_validator('ignore_missing')]
		})
		schema.update({
			'load_rdf_job_start': [tk.get_converter('convert_from_extras'),
								   tk.get_validator('ignore_missing')]
		})

		# CUSTOM LICENSE TO RESOURCE
		schema['resources'].update({
			'resource_license': [
				tk.get_validator('ignore_missing')]
		})
		schema['resources'].update({
			'resource_capacity': [tk.get_validator('default')('public')]


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
