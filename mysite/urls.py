from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', 'learn.views.index', name='home'),
    url(r'^home', 'learn.views.home', name='home'),
    url(r'^list', 'learn.views.list', name='list'),
    url(r'^admin/', include(admin.site.urls)),
)
