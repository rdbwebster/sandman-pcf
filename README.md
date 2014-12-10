sandman-pcf
===========

An example of the Python Sandman application deployed on Cloud Foundry
ooo

cf cups remote-mysql -p '{"host":"192.168.109.2","port":"3306","database":"customer_database","user":"bob","password":"welcome1"}'


python3.4 sandmanctl.py mysql+pymysql://bob:welcome1@localhost/customer_database
