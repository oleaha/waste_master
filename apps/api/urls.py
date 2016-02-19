from django.conf.urls import url
from apps.api import views

urlpatterns = [
    url(r'readings/$', views.container_reading_list)
]