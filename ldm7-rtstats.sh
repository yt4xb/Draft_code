#EXEC file to create & send ldm7-rtstats.log
while true
do
  LastTimeStamp=$(head -1 var/logs/ldmd.log | awk '{print $1}')
  DateStamp=$(echo $LastTimeStamp | sed 's/T.*$//g')
  sleep 59
  sed -n "/$LastTimeStamp/",'$p' var/logs/ldmd.log | sed -n '1,$p' >> var/logs/ldmd-$DateStamp.log
  sed -n "/$LastTimeStamp/",'$p' var/logs/ldmd.log | grep -E "Received:|Inserted:" | sed -n '2,$p' >& ldm7.log
  python util/ldm7-rtstats.py ldm7.log ldm7-rtstats.log HDS
  ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats.log
  ldmadmin newlog
done
