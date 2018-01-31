from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('applications/', include('applications.urls')),
    path('admin/', admin.site.urls),
]