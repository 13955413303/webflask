# webflask
一,MySQL
1.安装MySQL

sudo apt-get update
sudo apt-get install mysql-server

2.配置MySQL

2.1 初始化配置

sudo mysql_secure_installation

#1
VALIDATE PASSWORD PLUGIN can be used to test passwords...
Press y|Y for Yes, any other key for No: N (我的选项)

#2
Please set the password for root here...
New password: (输入密码)
Re-enter new password: (重复输入)

#3
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them...
Remove anonymous users? (Press y|Y for Yes, any other key for No) : N (我的选项)

#4
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network...
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : Y (我的选项)

#5
By default, MySQL comes with a database named 'test' that
anyone can access...
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : N (我的选项)

#6
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Y (我的选项)

2.2 检查mysql服务状态

systemctl status mysql.service

3.配置远程访问

在Ubuntu下MySQL缺省是只允许本地访问的，使用workbench连接工具是连不上的；如果你要其他机器也能够访问的话，需要进行配置；

3.1 首先用根用户进入

sudo mysql -uroot -p

GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY "123456";

3.2 新建数据库和用户

用root用户新建数据和用作远程访问的用户

##1 创建数据库weixx

CREATE DATABASE weixx;

##2 创建用户wxx(密码654321) 并允许wxx用户可以从任意机器上登入mysql
的weixx数据库

GRANT ALL PRIVILEGES ON weixx.* TO wxx@"%" IDENTIFIED BY "654321"; 

二,apache

apt install apache2

cp *.html /var/www/html/

service apache2 restart 

三,python

pip3 install PyMysql

pip3 install flask

四,service

cp webflask.service /etc/systemd/system

systemctl daemon-reload

systemctl start webflask

systemctl enable webflask


https://blog.csdn.net/weixx3/article/details/80782479
https://blog.csdn.net/lsoftp/article/details/94622797
https://www.cnblogs.com/jiading/p/11627771.html
