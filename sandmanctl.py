import os
import sys
import json
import sandman
from sandman import app

def main(argv):
       pythonPort = '5000'  #default for local execution
       host = ''
       port = ''
       user = ''
       password = ''

       print(str(len(sys.argv)))
       #normal command line start?
       if len(sys.argv) == 2:    
            url = argv[1];

       else:

            # Check if running on Cloud Foundry
            try:
                 sql_service = json.loads(os.environ['VCAP_SERVICES'])['user-provided'][0]
                 pythonPort = os.getenv('VCAP_APP_PORT') # Assigned port for app in Cloud Foundry
                 credentials = sql_service['credentials']
                 host = credentials['host']
                 port = credentials['port']
                 user = credentials['user']
                 password = credentials['password']
                 url="mysql+pymysql://" + user + ":" + password + "@" + host + ":" + port +  "/customer_database"

            except KeyError as e:
                 print ('Error: Could not locate VCAP_SERVICES env variable containing user provided service')
                 print ('       To run outside Cloud Foundry Supply command line parameters')
                 sys.exit(2)


       print('Python listening on Port: ' + str(pythonPort))
       print('Alchemy sql server url = ' + url)
       app.config['SQLALCHEMY_DATABASE_URI'] = url

       from sandman.model import activate
       activate()
       
       app.run(debug=False,port=int(pythonPort),host='0.0.0.0',threaded=True)

if __name__ == "__main__":
   main(sys.argv[0:])
