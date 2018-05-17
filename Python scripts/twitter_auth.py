# importing necessary libraries
import os
import sys
import json
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
	"""
	This function creates authentication object
	"""
	try:
		# user credentials to access the twitter API
		consumer_key = '3Rl1FjZob9Xkmqt4oL3aROQ8a'
		consumer_secret = 'lKh4c98UakktIehvWs0ZnuJe62jomMQZbtVU3KYH70rEYN2HBz'
		access_token = '994425047644172288-mCvKsFLvECePmdxpZkA5hLaLcbndtcU'
		access_token_secret = 'ZrgLVvINBAHpuJVBboTMisKfoRhjd5Is1o1DK8gaafTA8'
	except KeyError:
		sys.stderr.write("Twitter environment variables are not set\n")
		sys.exit()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return auth

def get_twitter_api():
	"""
	This function creates API object(setting up client)
	"""
	auth = get_twitter_auth()
	api = API(auth)
	return api

tweets_data=[]
def get_tweet_data():
	"""
	This function gets the tweets collected from the json file to a list
	"""
	# for seperation of concern
	tweets_data_path='./data/alltweets.json'
	tweets_file=open(tweets_data_path,"r") 
	for line in tweets_file:
		try:
			tweet = json.loads(line)
			tweets_data.append(tweet)
		except:
			continue
	return tweets_data

# def get_geo_json_data():
# 	"""
# 	This function gets the tweets collected from the json file to a list
# 	"""
# 	# for seperation of concern
# 	tweets_data_path='alltweets.json'
# 	geo_data = {
# 	    "type": "FeatureCollection",
# 	    "features": []
# 	    }
# 	tweets_file=open(tweets_data_path,"r") 
# 	for line in tweets_file:
# 		try:
# 			tweet = json.loads(line)
# 			if tweet['coordinates']:
#                 geo_json_feature={
#                     "type": "Feature",
#                     "geometry": tweet['coordinates'],
#                     "properties": {
#                         "text": tweet['text'],
#                         "created_at": tweet['created_at']
#                     }
#                 }
#                 geo_data['features'].append(geo_json_feature)
# 		except:
# 			continue
# 	return geo_data

