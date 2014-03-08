# app urls mentors/urls.py
from django.conf.urls import patterns, url

from mentors import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='mentors_home'),
	url(r'^mentor/$', views.mentorList, name='mentors_mentor_list'),
	url(r'^mentor/(?P<pk>\d+)$', views.mentor, name='mentors_mentor'),
	url(r'^afraid$', views.afraid, name='mentors_mentor'),
	url(r'^proud$', views.proud, name='mentors_mentor'),
	url(r'^skill/$', views.skillList, name='mentors_skill_list'),
	url(r'^skill/(?P<pk>\d+)$', views.skill, name='mentors_skill'),
	)