import fitbit
import ConfigParser
import json
from pprint import pprint
import matplotlib.pyplot as plt

#Setup an unauthorised client (e.g. with no user)

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

#b32029b998c848e1a5283ac30207893d
#b6800daaecb94e269e8425642269a2b5
#client = fitbit.FitbitOauthClient(consumer_key,consumer_secret)

#client = fitbit.FitbitOauthClient(consumer_key, consumer_secret)
#token = client.fetch_request_token()
#print 'FROM RESPONSE'
#print 'key: %s' % token
#print 'callback confirmed? %s' % str(token.callback_confirmed)
#print ''
USER_KEY = '4426e78f78128deb3ee0ed2e15ef9586'
USER_SECRET = 'e1c559b549b84ae0b9ba3cf958b8e393'

authd_client = fitbit.Fitbit(consumer_key,consumer_secret, resource_owner_key=USER_KEY,resource_owner_secret=USER_SECRET)

#fitbit_stats = authd_client._COLLECTION_RESOURCE('activities')
#print 'Activities:'
#print fitbit_stats

#fitbit_stats = authd_client._COLLECTION_RESOURCE('sleep')
#print 'Sleep:'
#print fitbit_stats

#fitbit_stats = authd_client.time_series('activities/steps',period='30d')
#print 'Timeseries:'
#print fitbit_stats

fitbit_stats = authd_client.time_series('activities/steps',period='1d')
#print 'Intraday:'
str_fitbit = str(fitbit_stats)
f = open("intraday.json","w")
json.dump(fitbit_stats,f)
#f.write(str_fitbit)
f.close()

json_data  = open("intraday.json","r")
data = json.load(json_data)
print(data.keys())
#steps = data['activities-steps']
steps = data['activities-steps-intraday']
data_steps = steps['dataset']
print(data_steps)
#pprint(steps)
#pprint(data)



#print '%s' % str(client)
#token = client.fetch_request_token()
#print 'FROM RESPONSE'
#print '%s' % str(token)

#activities_list()
#print 'key: %s' % str(token.key)
#print 'secret: %s' % str(token.secret)
#print 'callback confirmed? %s' % str(token.callback_confirmed)
#print ''
