from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	#/polls/
	url(r'^$', views.index, name = 'index'),
	#/polls/question id
	url(r'^(?P<question_id>\d+)/$', views.detail, name = 'detail'),
	#/polls/question id/results
	url(r'^(?P<question_id>\d+)/results/$', views.results, name = 'results'),
	#/polls/question id/vote
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name = 'vote'),
	
)