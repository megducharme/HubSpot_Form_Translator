from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'applications'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_csv$', views.upload_csv, name='upload_csv'),
    url(r'^show_applications/(?P<date>\d{4}-\d{2}-\d{2})/$', views.show_applications, name='show_applications'),
    url(r'^show_single_application/(?P<email>\D+)/', views.show_single_application, name='show_single_application'),
]