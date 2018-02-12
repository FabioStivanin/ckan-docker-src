import os
import ckan.lib.uploader as uploader
import cgi
import ckan.lib.munge as munge
import datetime
import ckan.logic as logic
import magic
from pylons import config




class CustomResourceUpload(object):

	def __init__(self, resource):

		path = uploader.get_storage_path()
		if not path:
			self.storage_path = None
			return
		self.storage_path = os.path.join(path, 'resources')
		try:
			os.makedirs(self.storage_path)
		except OSError, e:
			# errno 17 is file already exists
			if e.errno != 17:
				raise
		self.filename = None

		url = resource.get('url')
		upload_field_storage = resource.pop('upload', None)
		self.clear = resource.pop('clear_upload', None)

		if isinstance(upload_field_storage, cgi.FieldStorage):
			self.filename = upload_field_storage.filename
			self.filename = munge.munge_filename(self.filename)
			resource['url'] = self.filename
			resource['url_type'] = 'upload'
			resource['last_modified'] = datetime.datetime.utcnow()
			self.upload_file = upload_field_storage.file
		elif self.clear:
			resource['url_type'] = ''

	def get_directory(self, id):
		directory = os.path.join(self.storage_path, id[0:3], id[3:6])
		return directory

	def get_path(self, id):
		directory = self.get_directory(id)
		filepath = os.path.join(directory, id[6:])
		return filepath

	# CUSTOMIZATION #####################
	def upload(self, id, max_size=10):
		if not self.storage_path:
			return

		directory = self.get_directory(id)
		filepath = self.get_path(id)

		if self.filename:
			try:
				os.makedirs(directory)
			except OSError, e:
				if e.errno != 17:
					raise
			tmp_filepath = filepath + '~'
			output_file = open(tmp_filepath, 'wb+')
			self.upload_file.seek(0)
			current_size = 0

			while True:

				current_size = current_size + 1
				data = self.upload_file.read(2 ** 20)
				if not data:
					break

				"""
				# formati di file che potrebbero essere malevoli
				ckan.black_list.upload_mimetype_blacklist = application/exe application/octet-stream application/x-msdownload application/x-exe application/dos-exe vms/exe application/x-winexe application/msdos-windows application/x-msdos-program application/bin application/binary application/bat application/x-bat application/textedit application/x-sh
				"""

				mimetype = magic.from_buffer(data, mime=True)
		
				'''Check if the resource mimetype is blacklisted (defined in development.ini)'''
				
    				blacklist = config.get('ckan.black_list.upload_mimetype_blacklist', '').split()		
				#print blacklist

				#from ckan.lib import helpers
				#formati_ammissibili = helpers.resource_formats()
				#print formati_ammissibili.keys()			 

				if current_size == 1:
					if mimetype in blacklist:
						os.remove(tmp_filepath)
						raise logic.ValidationError(
							{'upload': ['Formato del file >> ' + str(mimetype)+' << illegale']}
						)
					#else:
					#	print 'Formato del file >> ' + str(mimetype)+' << accettato :-)'

				output_file.write(data)
				if current_size > max_size:
					os.remove(tmp_filepath)
					raise logic.ValidationError(
						{'upload': ['File upload too large']})
			output_file.close()
			os.rename(tmp_filepath, filepath)
			return

		if self.clear:
			try:
				os.remove(filepath)
			except OSError, e:
				pass	 