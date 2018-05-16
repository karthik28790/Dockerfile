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
mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "insert into table_name (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "insert into table_name (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "insert into table_name (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "insert into table_name (REMOTE_ADDR,REQUEST_METHOD) values('${REMOTE_ADDR}','${CLOCK}')"
HITS=$(mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM table_name")
HITS=$(mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM table_name")
HITS=$(mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM table_name")
HITS=$(mysql -h MySQL_db_HOST -u USER -pPASSWORD -Pport -Ddatabase -e "SELECT COUNT(*) as "No_of_WebsiteHits_sofar" FROM table_name")
echo "No of Website Hits - $HITS"
echo '</body>'
echo '</html>'
exit 0
