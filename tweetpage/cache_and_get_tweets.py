import random
from django.core.cache import cache

politician_screen_names = ['barackobama', 'hillaryclinton', 'joebiden', 'billclinton', 'nancypelosi', 
	'johnboehner', 'stevescalise', 'mittromney', 'mcconnellpress', 'senatorreid'] 

# triggers a cache set if it's empty and returns a list of four tweets
def fetch_cached_tweets():
	full_tweet_list = cache.get("tweets")
	if full_tweet_list is None:
		full_tweet_list = fetch_all_tweets()
		cache.set("tweets", full_tweet_list, 60*15) # caches tweets for 30 min
	return fetch_four_rand_tweeters()
	
	
# gets user timelines for all politicians	
def fetch_all_tweets():
	try:
		import twitter
		api = twitter.Api(consumer_key='CcFvFZ9bOBNBVDdsZ1d532bQu', consumer_secret='B7eVvlDMrTrbihnu99CFswtnBiWEKw8tAjL3UfgMwVspXQ7l7X', access_token_key='3169384915-KifaOavehaTuJS4CSYrRoM7demWLQxFuAYBZ9Gj', access_token_secret='P9xx5gU2GrRoURdoHcE8QxlDC5thxwGckNXTCUCrLOAaL')
		user_lst = []
		for name in politician_screen_names:
			user = api.GetUserTimeline(screen_name=name, include_rts=False, exclude_replies=True, count=200)
			user_lst.append(user)
	except:
		tweets.append({'user': {'name': 'Error', 'screenname': 'Error'}, 'text': 'Error'})
	return user_lst		


# gets the user timeline for four unique random politicians from the cache
def fetch_four_rand_tweeters():
	rand_tweet_num = random.randint(0,99) # generates a random number to grab one of user's the last 10 tweets
	rand_screen_name_nums = generate_rands(len(politician_screen_names)) # gets 4 unique random numbers btw 0 and the length of the politician_screen_names
	user_lst_four = []
	for num in rand_screen_name_nums:
		user = cache.get("tweets")[num]
		user_lst_four.append(user[rand_tweet_num])
	user_lst_four[0].text = process_text(user_lst_four[0].user.name, user_lst_four[0].text) # processes the displayed tweet's text
	return user_lst_four


# returns a list with 4 random, unique numbers no greater than index - 1
def generate_rands(index):
	rands = []
	while len(rands) < 4:
		randnum = random.randint(0, index-1)
		if randnum not in rands:
			rands.append(randnum)
	return rands

# removes instances of the tweeter's name from the tweet and character codes with the proper character
def process_text(name, tweet):
	name_parts = name.split(" ")
	if "" in name_parts:
		name_parts.remove("")
	tweet = tweet.replace('&amp', '&').replace('&gt', '>').replace('&lt', '<')
	for str in name_parts:
		tweet = tweet.replace(str, "*****")
	return tweet