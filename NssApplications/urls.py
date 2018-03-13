from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('applications.urls')),
    path('admin/', admin.site.urls),
]
