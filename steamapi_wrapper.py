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

	def get_interface_names(self):
		for x in self.api_options:
			print x

	def call_api(self, interface, method=None):
	    interface_options = {}
	    if self.api_options[interface]:
	        for x, y in list(enumerate(self.api_options[interface])):
	            interface_options[y['name']] = x

	    if method is None:
	    	# If no method argument is supplied, print all available method options for the interface.
	    	for x in interface_options:
	    		print x
		else:
			# with interface, method, interface_options[method], build off get_api_list to capture version.
			# print 'http://api.steampowered.com/%s/%s/v%s/?' % (interface, method, interface_options[method])
			print 'Testing (wtf else the first condition went through!)'

## Testing... going to finish the query build for this function.
## Advanced steam api queries will call to this query builder in later functions.

steam = Steam_API()
print steam.call_api('ICSGOServers_730')
# testing method=None with the second steam.call_api argument: 'GetGameServersStatus'
