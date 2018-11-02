#EXEC file to create & send ldm7-rtstats.log
python ldm7-rtstats.py /home/ldm7/var/logs/ldmd.log ldm7-rtstats-fdt.log
ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats-fdt.log
sleep 60
