# importing necessary libraries
import tweepy
from twitter_auth import get_twitter_api, get_tweet_data

if __name__ == '__main__':
	api = get_twitter_api()

def get_total_tweets():
	"""
	This function returns total number of tweets in integer
	"""
	tweet_data = get_tweet_data()
	return len(tweet_data)

def get_unique_users():
	"""
	This function reads the tweet data and fetches unique users from collected data
	"""
	allUsers=[]
	tweet_data = get_tweet_data()
	for eachTweet in tweet_data:
		allUsers.append(eachTweet['user']['name'])
	uniqueUsers = set(allUsers)
	return uniqueUsers

def get_tweets_with_media():
	"""
	This function returns number of tweets with media
	"""
	tm=0
	tweet_data = get_tweet_data()
	for eachTweet in tweet_data:
		if 'media' in eachTweet['entities']:
			tm=tm+1
		else:
			continue
	return tm

def get_most_retweeted_tweet():
	"""
	This function returns the tweet that has maximum number of retweets
	"""
	max_rt_count=0
	rt_tweet=""
	tweet_data = get_tweet_data()
	for eachTweet in tweet_data:
		try:
			if eachTweet['retweeted_status']['retweet_count'] > max_rt_count:
				max_rt_count = eachTweet['retweeted_status']['retweet_count']
				rt_tweet = eachTweet['text']
		except KeyError as e:
			continue
		
	return rt_tweet

def get_most_favorite_tweet():
	"""
	This function returns the tweet that has maximum number of retweets
	"""
	max_fav_count=0
	fav_tweet=""
	tweet_data = get_tweet_data()
	for eachTweet in tweet_data:
		try:
			if eachTweet['retweeted_status']['favorite_count'] > max_fav_count:
				max_fav_count = eachTweet['retweeted_status']['favorite_count']
				fav_tweet = eachTweet['text']
			# print(eachTweet['retweeted_status']['text'])
		except KeyError as e:
			continue
	return fav_tweet

def get_tweet_count_by_location():
	"""
	This function returns tweet count of each location
	"""
	location_list=[]
	tweet_data = get_tweet_data()
	for eachTweet in tweet_data:
		location_list.append(eachTweet['user']['location'])
	return location_list

