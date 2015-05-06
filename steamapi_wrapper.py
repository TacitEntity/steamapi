import requests
import json

import pprint

class Steam_API(object):
## Wrapper for Steam API ##	
# http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>
	def __init__(self):
		with open('userInfo.json', 'r') as inFile:
			self.userInfo = json.load(inFile)

		self.api_list = 'http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key='
		self.get_api_list = requests.get(self.api_list + self.userInfo['auth_key']).json()['apilist']['interfaces']
		self.api_options = {}
		for interface_name in self.get_api_list:
			self.api_options[interface_name['name']] = interface_name['methods']

	def get_options(self, known_interface=None):
	# grab a list of the interface and their method(s)
		if known_interface:
			print known_interface
			print '----------------------------'
			for method in self.api_options[known_interface]:
				print method['name']

		else:
			for interface in self.api_options.keys():
				print '============================'
				print interface
				print '----------------------------'
				for method in self.api_options[interface]:
					print method['name']

	def call_api(self, interface, method):
	    self.interface_options = {}
	    if self.api_options[interface]:
	    	# grab the index of the method for the specified interface
	        for x, y in list(enumerate(self.api_options[interface])):
	            self.interface_options[y['name']] = x

	    if self.interface_options[method]:
	    	# pull the interface, the method, and pull version to create the query
	    	print 'http://api.steampowered.com/%s/%s/v%s/?' % (interface, method, self.api_options[interface][self.interface_options[method]]['version'])

## Advanced steam api queries will call to this query builder in later functions.
steam = Steam_API()

steam.get_options('ISteamUserStats')

# for testing index and version control (change the index to account for the method)
# steam.call_api('ISteamUserStats', 'GetSchemaForGame')
# print steam.api_options['ISteamUserStats'][6]