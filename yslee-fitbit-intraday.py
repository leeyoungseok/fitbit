import fitbit
import ConfigParser
import json
from pprint import pprint
import matplotlib.pyplot as plt

#Load Settings
parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')
consumer_key = parser.get('Login Parameters', 'C_KEY')
consumer_secret = parser.get('Login Parameters', 'C_SECRET')
 
#Setup an unauthorised client (e.g. with no user)
unauth_client = fitbit.Fitbit(consumer_key, consumer_secret)

#Get data for a user
user_params = unauth_client.user_profile_get('2724VX')

print "%s" % user_params

#USER_KEY = 'your key'
#USER_SECRET = 'your secret'

authd_client = fitbit.Fitbit(consumer_key,consumer_secret, resource_owner_key=USER_KEY,resource_owner_secret=USER_SECRET)

fitbit_stats = authd_client.time_series('activities/steps',period='1d')
str_fitbit = str(fitbit_stats)
f = open("intraday.json","w")
json.dump(fitbit_stats,f)
f.close()

json_data  = open("intraday.json","r")
data = json.load(json_data)
print(data.keys())
steps = data['activities-steps-intraday']
data_steps = steps['dataset']
print(data_steps)
