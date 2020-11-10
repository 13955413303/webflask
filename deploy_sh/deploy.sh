#!/bin/bash

get_ip=`ifconfig | grep ens -A 2| grep 192.|awk '{print $2}'`
old_ip=`cat ../sql_util/link_mysql.py | grep 192.168|awk -F '"' '{print $2}'`
sed -i "s/${old_ip}/${get_ip}/g" ../html/*.html
sed -i "s/${old_ip}/${get_ip}/g" ../sql_utl/link_mysql.py
cp ../html/*.html /var/www/html/
cp ./webflask.service /etc/systemd/system/


