import sys
import string
import json
ports = []
filename = sys.argv[1]
logname = sys.argv[2]
with open(filename, 'r+') as f:
    jsonData = json.load(f)
f.close()
searchResults1 =  jsonData
#for er in searchResults1:
#	print er
#	if er[0] == "success":
#		node.append(er['domains'][0]['nodes'][0]['address'])
#node_id = searchResults1['domains'][0]['nodes'][0]['id']
domains = searchResults1['domains'][0]
nodes = domains['nodes'][0]
node_address = nodes['address']
ports = nodes['ports'][0]
links = ports['links']
#for key, value in searchResults1.iteritems():
#	print key, value

data = {"withlocation": 0, "topology" : {"nodes": node_address, "links" : links}}
with open(logname, 'w+') as l:	
    json.dump(data, l)
l.close()

#for i in ports:
#	print i
#searchResults2 =  jsonData2['results']
#for er in searchResults2:
#	if er['link'] != None:
#		link.append(er['link'])
print node_address
