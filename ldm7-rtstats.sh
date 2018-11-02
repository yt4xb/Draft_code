#EXEC file to create & send ldm7-rtstats.log
python ldm7-rtstats.py var/logs/ldmd.log ldm7-rtstats.log
ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats.log
sleep 60
