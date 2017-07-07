from django.conf.urls import url

from . import views

app_name = 'news'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^/$', views.news, name='news'),
    url(r'^team/$', views.team, name='team'),
    url(r'^reference/$', views.reference, name='reference'),
    #url(r'^admin/$', views.admin, name='admin'),
    url(r'^$', views.index, name='index'),
    #url(r'^admin/news$', views.admin_news, name='admin_news'),
    #url(r'^admin/aboutus$', views.aboutus, name='aboutus'),
    url(r'^(?P<id>[0-9]+)/$', views.fullread, name='fullread'),
]
