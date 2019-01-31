import sys
import string
import json
tmp1 = []
tmp2 = []
tmp3 = []
links = []
filename = sys.argv[1]
logname = sys.argv[2]
with open(filename, 'r+') as f:
    jsonData = json.load(f)
f.close()
topology =  jsonData['topology']
node = topology['nodes']
link = topology['links']
for er in link:
	#source = er['source']
	target = er['target']
	#tmp1 = source.split(":")
	#a,b = tmp1[4].split("=")	
	tmp2 = target.split(":")
	for fr in node:
		node_id = fr['id']
		x = er['trafficEngineeringMetric']
		if int(x) < 50000:	
		    if tmp2[4] != node_id:
			tmp = {"id" : er['id'], "source" : node_id, "target" : tmp2[4], "capacity" : er['capacity'], "MTU" : er['MTU'], "group" : "N/A", "loss": "N/A", "delay": "N/A", "bandwidth": "N/A", "max_queue_size": "N/A", "use_htb": "N/A"}
			links.append(tmp)

data = {"withlocation": 0, "topology" : {"nodes": node, "links" : links}}

with open(logname, 'w+') as l:	
    json.dump(data, l)
l.close()

