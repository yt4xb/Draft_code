import sys
import string
import json
node = []
ports = []
links = []
node_name = []
filename = sys.argv[1]
logname = sys.argv[2]
with open(filename, 'r+') as f:
    jsonData = json.load(f)
f.close()
searchResults1 =  jsonData['domains']
nodes = searchResults1['nodes']

for er in nodes:
	node_id = er['id']
	node_name = node_id.split(":")
	a, b = node_name[4].split("=") 
	tmp1 = {"id" : b, "ip" : er['address']}
	node.append(tmp1)
	ports.append(er['ports'])
	for fr in er['ports']:
		for gr in fr['links']:
			tmp2 = {"id" : gr['id'], "source" : er['id'], "target" : gr['remoteLinkId'], "capacity" : fr['capacity'], "MTU" : gr['interfaceMTU']}
			links.append(tmp2)


data = {"withlocation": 0, "topology" : {"domain" : "es.net", "nodes": node, "links" : links}}

with open(logname, 'w+') as l:	
    json.dump(data, l)
l.close()

