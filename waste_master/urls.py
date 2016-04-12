from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.frontend.views import login_view, profile_view, logout_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waste_master.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', login_view, name='login'),
    url(r'^profile/', profile_view, name='profile'),
    url(r'^logout/', logout_view, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apps.api.urls')),
)
