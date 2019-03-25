#EXEC file to create & send ldm7-rtstats.log
while true
do
  LastTimeStamp=$(tail -1 var/logs/ldmd.log | awk '{print $1}')
  sleep 600
  sed -n "/$LastTimeStamp/",'$p' var/logs/ldmd.log | grep -E "Received:|Inserted:" | sed -n '2,$p' >& ldm7.log
  python util/ldm7_rate_stats.py ldm7.log ldm7-rate.json NGRID
  python ldm_rate.py ldm7-rate.json
done
