# web framework
import cherrypy


# our stuff
from tools.db import objects
from tools import config
from base_webpage import BaseWebPage



class SetupsPage(BaseWebPage):
	
	def __init__(self):
		super(SetupsPage, self).__init__(objects.Zone)
		self.fields['id'] = {'name':'ID', 'visible':['list']}
		self.fields['name'] = {'name':'Name', 'visible':['list', 'add', 'update']}
		self.fields['description'] = {'name':'Description', 'visible':['list', 'add', 'update']}
		#self.fields['active'] = {'name':'Active', 'visible':['list', 'add', 'update']}


	@cherrypy.expose
	def index(self, flash_message=None):
		tmpl = self.lookup.get_template("setups.mako")
		return tmpl.render(page_title="Setups", flash_message=flash_message)





