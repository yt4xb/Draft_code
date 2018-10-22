#EXEC file to create & send ldm7-rtstats.log
cat /home/ldm7/var/logs/ldmd.log | grep mldm_receiver.c | awk '{print $1"\t"$8"\t"$7"\t"$5"\t"$9}' > ldm7-rtstats-fdt.csv
ldmadmin newlog
python parse.py ldm7-rtstats-fdt.csv ldm7-rtstats-fdt.log
ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats-fdt.log
sleep 60
