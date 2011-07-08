import frontik
import json
import garry.handler

class Page(garry.handler.PageHandler):
	def get_page(self):
		
		self.set_template('index.tmpl')
	
		def search(xml, response):
			self.Dict["search"] = json.loads(response.body)
		
		def employer(xml, response):
			self.Dict["employer"] = json.loads(response.body)
		
		self.get_url("http://api.hh.ru/1/json/vacancy/search/", callback=search)
		self.get_url("http://api.hh.ru/1/json/vacancy/employer/1455", callback=employer)
