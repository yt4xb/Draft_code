import sys
import string
import json
import networkx as nx
G=nx.Graph()
paths = []
nodes = []
path = []
links = []
filename = sys.argv[1]
logname = sys.argv[2]
with open(filename, 'r+') as f:
    jsonData = json.load(f)
f.close()
topology =  jsonData['topology']
node = topology['nodes']
link = topology['links']
for er in node:
    tmp = er['id']
    nodes.append(str(tmp))
G.add_nodes_from(nodes)
for er in node:
    tmp_source = er['id']
    path.append(tmp_source)
    for fr in link:
        link_source = fr['source']
        if tmp_source == link_source:
            tmp_target = fr['target']
            path.append(tmp_target)
            for lr in paths:
                if path == lr:
                    path = []
            if path != []:
                paths.append(path)
                G.add_edge(str(tmp_source), str(tmp_target))
                path = []
paths = []
with open(logname, 'w+') as l:
	for i in nodes:
		path = nx.single_source_shortest_path(G, i)
		tmp = {i:path}		
		json.dump(tmp, l)
		paths.append(path)		
l.close()
