from tweepy import cursor
from twitter_auth import get_twitter_api, get_tweet_data


# max_fav_count=0
# max_rt_count=0

u=0
query = "#vivoipl"
maxt = 100
if __name__ == '__main__':
	api = get_twitter_api()
	# tweets_data=api.search(q=query, rpp=maxt)
	tweets_data = get_tweet_data()

def get_total_tweets():
	"""
	This function returns total number of tweets in integer
	"""
	return len(tweets_data)

def get_unique_users():
	"""
	This function reads the tweet data and fetches unique users from collected data
	"""
	allUsers=[]
	for eachTweet in tweets_data:
		allUsers.append(eachTweet['user']['name'])
	uniqueUsers = set(allUsers)
	return uniqueUsers

def get_tweets_with_media():
	"""
	This function returns number of tweets with media
	"""
	tm=0
	for eachTweet in tweets_data:
		if 'media' in eachTweet['entities']:
			tm=tm+1
		else:
			pass
	return tm

def get_most_retweeted_tweet():
	"""
	This function returns the tweet that has maximum number of retweets
	"""
	max_rt_count=0
	rt_tweet=""
	for eachTweet in tweets_data:
		if eachTweet['retweet_count'] > max_rt_count:
			max_rt_count = eachTweet['retweet_count']
			rt_tweet = eachTweet['text']
		else:
			continue
	return rt_tweet

def get_most_favorite_tweet():
	"""
	This function returns the tweet that has maximum number of retweets
	"""
	max_fav_count=0
	fav_tweet=""
	for eachTweet in tweets_data:
		# print(eachTweet.favorite_count)
		if eachTweet['favorite_count'] > max_fav_count:
			max_fav_count = eachTweet['favorite_count']
			fav_tweet = ['eachTweet.text']
		else:
			continue
	return fav_tweet

def get_tweet_count_by_location():
	"""
	This function returns tweet count of each location
	"""
	location_list=[]
	for eachTweet in tweets_data:
		location_list.append(eachTweet['user']['location'])
	return location_list

# Total number of tweets
print("Total number of tweets : {}".format(get_total_tweets()))

#  displayed unique users
uniqueUsers = get_unique_users()
for user in uniqueUsers:
		print("User {a} = {b}".format(a=u, b=user))
		u=u+1

# displaying tweets with media
print("Tweets with media = {}".format(get_tweets_with_media()))

# displaying most favorite tweet
# get_most_favorite_tweet()
print("The most favorite tweet : {}".format(get_most_favorite_tweet()))

# displaying most retweeted tweet
print("The most retweeted tweet : {}".format(get_most_retweeted_tweet()))



# getting tweets by location 
location_list = get_tweet_count_by_location()
location_list_set = set(location_list)
for loc in location_list_set:
	print("{a} = {b}".format(a=loc, b=location_list.count(loc)))	


# 2. UNIQUE USERS
# allUsers=[]
# if __name__ == '__main__':
# 	api = get_twitter_api()
# 	public_tweet = api.home_timeline()
# 	for tweet in public_tweet:
# 		allUsers.append(api.get_user(id=tweet.user.id).name)
# 	uniqueUsers=set(allUsers)
# 	i=1
# 	for user in uniqueUsers:
# 		print("User {a} = {b}".format(a=i, b=user))
# 		i=i+1

# 3. COUNTS OF TWEET WITH MEDIA
# i=0
# if __name__ == '__main__':
# 	api = get_twitter_api()
# 	public_tweet = api.home_timeline()
# 	for tweet in public_tweet:
# 		if 'media' in tweet.entities:
# 			i=i+1
# 		else: 
# 			pass

# 	print(i)




# 5. TWEET WITH MOST FAVORITE COUNT
# public_tweet = api.home_timeline()
# 	for tweet in public_tweet:
# 		print("Favourite tweet count  = {}".format(tweet.favorite_count))
# 		if tweet.favorite_count > max_fav_count:
# 			max_fav_count = tweet.favorite_count
# 			fav_tweet = tweet.text
# 	print("Most favorite tweet : {}".format(fav_tweet))


# 4. MOST RETWEETS
# public_tweet = api.home_timeline()
# 	for tweet in public_tweet:
# 		print("Re tweet count  = {}".format(tweet.retweet_count))
# 		if tweet.retweet_count > max_rt_count:
# 			max_rt_count = tweet.favorite_count
# 			rt_tweet = tweet.text
# 	print("Most retweeted tweet : {}".format(rt_tweet))