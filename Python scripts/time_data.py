# importing necessary libraries
import tweepy
import csv
from twitter_auth import get_tweet_data

time_list = []

# Open/create a file to append data to
csvFile = open('time_count.csv', 'a')
#Use csv writer
csvWriter = csv.writer(csvFile)

if __name__ == '__main__':
	tweet_data = get_tweet_data()

# getting tweet date and time
for eachTweet in tweet_data:
	time_list.append(eachTweet['created_at'])

# extracting only time
time_list_tt = []
for time in time_list:
 	time_list_tt.append(time[11:16])

# getting time in minutes, removing repetitions
time_list_set1 = set(time_list_tt)
time_list_set = sorted(time_list_set1)

# storing the time along with the count in csv file
for time in time_list_set:
	csvWriter.writerow([time_list_tt.count(time),time])
csvFile.close()
# print("{a} = {b}".format(a=time,b=time_list_tt.count(time)))