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
#unauth_client = fitbit.Fitbit(consumer_key, consumer_secret)

#Get data for a user
#user_params = unauth_client.user_profile_get('2724VX')
#print "%s" % user_params

USER_KEY = '4426e78f78128deb3ee0ed2e15ef9586'
USER_SECRET = 'e1c559b549b84ae0b9ba3cf958b8e393'

authd_client = fitbit.Fitbit(consumer_key,consumer_secret, resource_owner_key=USER_KEY,resource_owner_secret=USER_SECRET)

fitbit_stats = authd_client._COLLECTION_RESOURCE('sleep')
print 'Sleep:'
print fitbit_stats

fitbit_stats = authd_client.time_series('activities/steps',period='30d')
print 'Timeseries:'
print fitbit_stats

