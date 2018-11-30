#EXEC file to create & send ldm7-rtstats.log
while true
do
  LastTimeStamp=$(tail -1 var/logs/ldmd.log | awk '{print $1}')
  sleep 60
  sed -n "/$LastTimeStamp/",'$p' var/logs/ldmd.log | sed -n '2,$p' >& ldm7.log
  python util/ldm7-rtstats.py ldm7.log ldm7-rtstats.log
  ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats.log
done
