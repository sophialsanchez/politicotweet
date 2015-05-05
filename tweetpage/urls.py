from django.conf.urls import include, url
import views

urlpatterns = [
	url(r'^$', views.start, name='start'),
	url(r'guess/$', views.post_list, name='guess'),
	url(r'^(?P<slug>[-\w]+)/$', views.Summary.as_view(), name='summary'),
]