#!/bin/bash
echo "Content-type: text/html"
echo ""
echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>No_of_WebsiteHits_sofar</title>'
echo '</head>'
echo '<body>'
CLOCK=$(date +%d%b%y"_"%T)
mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "insert into docker_table (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "insert into docker_table (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "insert into docker_table (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "insert into docker_table (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
HITS=$(mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM docker_table")
HITS=$(mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM docker_table")
HITS=$(mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM docker_table")
HITS=$(mysql -h 34.229.201.47 -u admin -padmin@123 -P4011 -Ddocker_db -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM docker_table")
echo $HITS
echo '</body>'
echo '</html>'
exit 0
