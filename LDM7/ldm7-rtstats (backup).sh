#EXEC file to create & send ldm7-rtstats.log
while true
do
  LastTimeStamp=$(date -u +'%Y%m%dT%H%M%S')
  DateStamp=$(echo $LastTimeStamp | sed 's/..$//g')
  echo $LastTimeStamp
  echo $DateStamp
  sleep 59
#  ldmadmin newlog
#  sed -n "/$LastTimeStamp/",'$p' var/logs/ldmd.log  >> var/logs/ldmd-$DateStamp.log
#  sed -n "/$LastTimeStamp/",'$p' var/logs/ldmd.log | grep -E "Received:|Inserted:" | sed -n '2,$p' >& ldm7.log
  cat var/logs/ldmd.log | grep $DateStamp | grep -E "Received:|Inserted:" >& ldm7.log
#  python util/ldm7-rtstats.py ldm7.log ldm7-rtstats.log HDS
#  ldmsend -v -h idc-uva.dynes.virginia.edu -P 38800 ldm7-rtstats.log
done
