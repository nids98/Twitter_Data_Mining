# importing necessary libraries from tweepy
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# user credentials to access the twitter API
consumer_key = '3Rl1FjZob9Xkmqt4oL3aROQ8a'
consumer_secret = 'lKh4c98UakktIehvWs0ZnuJe62jomMQZbtVU3KYH70rEYN2HBz'
access_token = '994425047644172288-mCvKsFLvECePmdxpZkA5hLaLcbndtcU'
access_token_secret = 'ZrgLVvINBAHpuJVBboTMisKfoRhjd5Is1o1DK8gaafTA8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#Here api is the entry point for most of the operations we perform with twitter
api = tweepy.API(auth)