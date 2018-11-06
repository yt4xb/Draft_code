#EXEC file to create & send ldm7-rtstats.log
while true
do
<<<<<<< HEAD
  python util/ldm7-rtstats.py var/logs/ldmd.log ldm7-rtstats.log
=======
  python ldm7-rtstats.py var/logs/ldmd.log ldm7-rtstats.log
>>>>>>> cac51d6254019309400cad57eba5434ce2437b99
  ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats.log
  sleep 60
done
