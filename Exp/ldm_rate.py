import sys
import json
from subprocess import call
filename = sys.argv[1]
f = open(filename, 'r')
jsonData = json.load(f)
IFACE_NAME = jsonData['iface']
TC_RATE = jsonData['tc_rate']
TC_BUFFER = jsonData['tc_buffer']
call('tc qdisc del dev %s root' % IFACE_NAME, quiet=True)
call('tc qdisc add dev %s root handle 1: htb default 2' % IFACE_NAME, quiet=True)
call('tc class add dev %s parent 1: classid 1:1 htb rate %smbit \
            ceil %smbit' % (IFACE_NAME, str(TC_RATE), str(TC_RATE)), quiet=True)
call('tc qdisc add dev %s parent 1:1 handle 10: bfifo limit %sb' %
            (IFACE_NAME, TC_BUFFER), quiet=True)
call('tc class add dev %s parent 1: classid 1:2 htb rate %smbit \
            ceil %smbit' % (IFACE_NAME, str(TC_RATE), str(TC_RATE)), quiet=True)
call('tc qdisc add dev %s parent 1:2 handle 11: bfifo limit %sb' %
            (IFACE_NAME, TC_BUFFER), quiet=True)
call('tc filter add dev %s protocol ip parent 1:0 prio 1 u32 match \
            ip dst 224.0.0.1/32 flowid 1:1' % IFACE_NAME, quiet=True)
call('tc filter add dev %s protocol ip parent 1:0 prio 1 u32 match \
            ip dst 0/0 flowid 1:2' % IFACE_NAME, quiet=True)
