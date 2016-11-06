from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings
from mwb import views
from mwb import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mwb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login',views.login_view),
    url(r'^accounts/login/$',  views.register_sesh),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summary/page=(?P<page>\d{1})$', views.summary, name='summary'),
    url(r'^prediction-accumulator', views.acca, name='acca'),
    url(r'^prediction-goals', views.goals, name='goals'),
    url(r'^prediction-exact-score', views.exact_score, name='exact_score'),
    url(r'^prediction-shocks', views.shocks, name='shocks'),
    #url(r'^pandata', views.pdata, name='pdata'),
    url(r'^indepth=(?P<data>[\w\,&]+)$', views.indepth, name='indepth'),
    url(r'^indepth', views.indepth, name='indepth'),
    url(r'^bet/data=(?P<data>[\w\,&]+)$', views.bet, name='bet'),
    url(r'^register.html', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^prob', views.prob_form,name='prob'),
    url(r'^testarray', views.bet ,name='testarray'),
    url(r'^about', views.about ,name='about'),
(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_ROOT}),
)
