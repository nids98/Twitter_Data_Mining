# importing necessary libraries
from tweet_analyse import *

# get total number of tweets
print("Total number of tweets = {}".format(get_total_tweets()))

#  displayed unique users
u=0
uniqueUsers = get_unique_users()
for user in uniqueUsers:
	print("User {a} = {b}".format(a=u, b=user))
	u=u+1

# displaying tweets with media
print("Tweets with media = {}".format(get_tweets_with_media()))

# displaying most retweeted tweet
print("The most retweeted tweet : {}".format(get_most_retweeted_tweet()))

# displaying most favorite tweet
print("The most favorite tweet : {}".format(get_most_favorite_tweet()))

# getting tweets by location 
location_list = get_tweet_count_by_location()
location_list_set = set(location_list)
for loc in location_list_set:
	print("{a} = {b}".format(a=loc, b=location_list.count(loc)))	