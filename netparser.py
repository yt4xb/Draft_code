import sys
import string
import json

with open('network.json') as f:
    jsonData = json.load(f)

searchResults1 =  jsonData['domains']['nodes']
for er in searchResults1:
	if er['ports'] != None:
		ports.append(er['ports']['id'])
for i in ports:
	print i
#searchResults2 =  jsonData2['results']
#for er in searchResults2:
#	if er['link'] != None:
#		link.append(er['link'])
