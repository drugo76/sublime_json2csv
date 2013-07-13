import sublime, sublime_plugin

import simplejson as json
import csv
import cStringIO
import os

class Json2csvCommand(sublime_plugin.TextCommand):

	# 1 - get the content of the json file or selection
	def get_json_content(self):
		regions = self.view.sel()
		if len(regions) > 0 and not regions[0].empty():
			selection = regions[0]
		else:
			selection = sublime.Region(0, self.view.size())

		return self.view.substr(selection)

	# 2 - write data to csv
	def write_csv(self, csv_buffer):
		write_header = True
		item_keys    = []
		writer       = csv.writer(csv_buffer)

		for item in self.data:
			item_values = []

			for key in item:
				if write_header:
					item_keys.append(key)

				item_values.append(item[key].encode('utf-8'))

			if write_header:
				writer.writerow(item_keys)
				write_header = False

			writer.writerow(item_values)	

	def run(self, edit):
		self.data            = []
		self.source_filename = self.view.file_name()
		print self.source_filename

		json_content = self.get_json_content()

		# validate json data
		try:
			print "json data is valid"
			self.data = json.loads(json_content)
			
			if self.source_filename:
				dest_filename = os.path.splitext(self.source_filename)[0] + '.csv'
				with open(dest_filename, 'wb') as csv_buffer:
					self.write_csv(csv_buffer)

				sublime.active_window().open_file(dest_filename)
			else:
				csv_buffer = cStringIO.StringIO()
				self.write_csv(csv_buffer)

				window = self.view.window()
				csv_file_view = window.new_file()
				selection = sublime.Region(0, csv_file_view.size())
				print selection

				edit = csv_file_view.begin_edit('json2csv')
				csv_file_view.replace(edit, selection, csv_buffer.getvalue())
				csv_file_view.end_edit(edit)				

		except Exception:
			import sys
			exc = sys.exc_info()[1]
			sublime.status_message(str(exc))
			print str(exc)
