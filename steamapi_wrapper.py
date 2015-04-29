import requests
import json

import pprint

class Steam_API(object):
## Wrapper for Steam API ##	
# http://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>
	def __init__(self):
		with open('userInfo.json', r) as inFile:
			userInfo = json.load(inFile)

		api_list = 'http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key='
		get_api_list = requests.get(api_list + userInfo['auth_key']).json()['apilist']['interfaces']
		api_options = {}
		for interface_name in get_api_list:
			api_options[interface_name['name']] = interface_name['methods']
		
		return api_options

	def call_api(interface, method=None):
	    interface_options = {}
	    if api_options[interface]:
	        print interface
	        for x, y in list(enumerate(api_options[interface])):
	            interface_options[y['name']] = x


print call_api('IDOTA2Fantasy_205790')
