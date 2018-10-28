#!/bin/bash
apk add --no-cache mysql-client
count=0
result=""
while [ "$result" != "mysqld is alive" ]; do
  count=`expr $count + 1`
  result=`mysqladmin ping -h mysql -u guestbook -pguestbook_pass` 
  if [ $count -gt 9 ]; then
    exit 1
  fi
  echo 'COUNT:'$count
  sleep 10
done
python manage.py test --settings sampleapp.settings_prod --noinput
