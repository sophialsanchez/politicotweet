from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView
from tweetpage.models import Result
from tweetpage import cache_and_get_tweets

def start(request):
	return render_to_response('tweetpage/start.html')


def post_list(request):
	context = {'tweet': cache_and_get_tweets.fetch_cached_tweets()}
	return render(request, 'tweetpage/index.html', context)


class Summary(DetailView):
	model = Result
	template_name = 'tweetpage/summary.html'
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(Summary, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the results
		context['result_list'] = Result.objects.all()
		return context

