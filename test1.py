import yaml
x = {"username" : "uva4api", "passwd":"edgar-polish-tower-alum"}
with open("account.yaml", "w") as output_stream:
	yaml.dump(x, output_stream, default_flow_style=False)
