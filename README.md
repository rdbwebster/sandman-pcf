sandman-pcf
===========

#### A project that demonstrates how to deploy the Python **Sandman** application on Cloud Foundry


##### Based on the Sandman project [https://github.com/jeffknupp/sandman](https://github.com/jeffknupp/sandman) 

Sandman is an amazing python application that auto-generates a REST api for all the entities in an existing SQL database.
When deployed to the Cloud Foundry platform its an extemely powerful tool for moderning access to SQL Server databases.
In fact when used with a Cloud Foundry [User Provided Service]( http://docs.cloudfoundry.org/devguide/services/user-provided.html)
the database to be REST enabled does not need to be running within the Cloud Foundry environment.  

##### Setup

When Sandman is deployed to Cloud Fondry the SQLAlchemy uri is contained in the Application Environment within Cloud Foundry.
The SQL Server resource must be exposed within Cloud Foundry as an advertised service, but it does not need to run within Cloud Foundry.

To connect to a remote sql server outside of Cloud Foundry create a UPS for example

```
cf cups remote-mysql -p '{"host":"192.168.109.2","port":"3306","database":"customer_database","user":"bob","password":"welcome1"}'
```

Then edit the manifest.xml file and set the defined service name in the services section.

##### Local Testing

Sandman can be run locally outside of cloud foundry to test its remote database connection.
For example
To run sandman outside of Cloud Foundry, and connect to the same database server the command line would be

```
python3.4 sandmanctl.py mysql+pymysql://bob:welcome1@localhost/customer_database
```

