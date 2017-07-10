from django.conf.urls import url

from . import views

app_name = "mynews"

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^/', views.news, name='news'),
    url(r'^teammembers/$', views.teammembers, name='teammembers'),
    url(r'^search/$', views.search, name='search'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^activity/$', views.activity, name='activity'),
    url(r'^monitoring/$', views.monitoring, name='monitoring'),
    url(r'^reference/$', views.reference, name='reference'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    #url(r'^admin/$', views.admin, name='admin'),
    url(r'^$', views.index, name='index'),
    #url(r'^admin/news$', views.admin_news, name='admin_news'),
    #url(r'^admin/aboutus$', views.aboutus, name='aboutus'),
    url(r'^fullread/(?P<id_news>[0-9]+)$', views.fullread, name='fullread'),
]
