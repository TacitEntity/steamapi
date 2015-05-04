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
		self.get_api_list = requests.get(api_list + userInfo['auth_key']).json()['apilist']['interfaces']
		self.api_options = {}
		for interface_name in self.get_api_list:
			self.api_options[interface_name['name']] = interface_name['methods']

	def call_api(self, interface, method=None):
	    interface_options = {}
	    if self.api_options[interface]:
	        print interface
	        for x, y in list(enumerate(self.api_options[interface])):
	            interface_options[y['name']] = x

s = Steam_API()
print s.call_api('IDOTA2Fantasy_205790')
