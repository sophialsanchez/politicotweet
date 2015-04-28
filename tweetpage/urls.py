from django.conf.urls import include, url
import views

urlpatterns = [
	url(r'^$', views.post_list, name='tweetpage'),
	url(r'summary/$', views.summary, name='summary'),
	url(r'^(?P<guesses>\d+)/(?P<num_correct>\d+)/(?P<match>\w+)/updateguesses/$', views.updateguesses, name='updateguesses'),
	url(r'start/$', views.start, name='start'),

]