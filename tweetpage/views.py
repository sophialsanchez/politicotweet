from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
import random
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def post_list(request):
	context = {'tweet': getTweet(), 'guessstats': {'guesses_left': 3, 'num_correct': 0}}
	return render_to_response('tweetpage/index.html', context, context_instance=RequestContext(request))


def summary(request, num_correct):
	context = num_correct
	return render_to_response('tweetpage/summary.html', context, context_instance=RequestContext(request))

def start(request):
	return render_to_response('tweetpage/start.html')

def updateguesses(request, guesses, num_correct, match):
	if (match == "True"):
		# increment num_correct and render tweetpage
		context = {'tweet': getTweet(), 'guessstats': {'guesses_left': guesses, 'num_correct': int(num_correct)+1}}
		return render_to_response('tweetpage/index.html', context, context_instance=RequestContext(request))
	else:
		# render summary page 
		if int(guesses) == 1:
			context = {'num_correct': num_correct}
			return render_to_response('tweetpage/summary.html', context, context_instance=RequestContext(request))
		# decrement guesses_left and render tweetpage
		else:
			context = {'tweet': getTweet(), 'guessstats': {'guesses_left': int(guesses)-1, 'num_correct': num_correct}}
			return render_to_response('tweetpage/index.html', context, context_instance=RequestContext(request))



# internal functions not called from URL

# returns a list of four tweets
def getTweet():
	tweets = []
	rand_tweet_num = random.randint(0,99) # generates a random number to grab one of user's the last 10 tweets
	politician_screen_names = ['barackobama', 'hillaryclinton', 'joebiden', 'billclinton', 'nancypelosi', 
	'johnboehner', 'gopleader', 'stevescalise', 'mittromney', 'mcconnellpress', 'senatorreid']
	rand_screen_name_nums = generate_rands(len(politician_screen_names)) # gets 4 unique random numbers btw 0 and the length of the politician_screen_names
	try:
		import twitter
		api = twitter.Api(consumer_key='CcFvFZ9bOBNBVDdsZ1d532bQu', consumer_secret='B7eVvlDMrTrbihnu99CFswtnBiWEKw8tAjL3UfgMwVspXQ7l7X', access_token_key='3169384915-KifaOavehaTuJS4CSYrRoM7demWLQxFuAYBZ9Gj', access_token_secret='P9xx5gU2GrRoURdoHcE8QxlDC5thxwGckNXTCUCrLOAaL')
		user_lst = []
		for num in rand_screen_name_nums:
			user = api.GetUserTimeline(screen_name=(politician_screen_names[num]), include_rts=False, exclude_replies=True, count=200)
			user_lst.append(user[rand_tweet_num]) # count is larger than rand_int_num to account for the missing retweets; should fix this so it's not just a guess
	except:
		tweets.append({'status': 'Follow us', 'date': 'about 10 min ago'})
	return user_lst

# returns a list with 4 random, unique numbers no greater than the index-1
def generate_rands(index):
	rands = []
	while len(rands) < 4:
		randnum = random.randint(0, index-1)
		if randnum not in rands:
			rands.append(randnum)
	return rands