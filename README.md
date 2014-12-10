sandman-pcf
===========

### An project that demonstrates how to deploy the Python Sandman application on Cloud Foundry


#### Based on the Sandman project    [https://github.com/jeffknupp/sandman](https://github.com/jeffknupp/sandman) 


### Setup

When Sandman is deployed to Cloud Fondry it obtains its SQLAlchemy uri from the Application Environment within Cloud Foundry.
The SQL Server resource must be exposed within Cloud Foundry as an advertised service, but it does not need to run within Cloud Foundry.
To connect to a remote sql server outside of Cloud Foundry create a [User Provided Service]( http://docs.cloudfoundry.org/devguide/services/user-provided.html)

For Example
cf cups remote-mysql -p '{"host":"192.168.109.2","port":"3306","database":"customer_database","user":"bob","password":"welcome1"}'

To run sandman outside of Cloud Foundry, but connecting to the same database server the command line would be

python3.4 sandmanctl.py mysql+pymysql://bob:welcome1@localhost/customer_database

