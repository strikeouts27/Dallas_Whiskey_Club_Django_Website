#Dallas_Whiskey_Club_Django_Website/
from django.contrib import admin
from django.urls import path, include
from .views import homepageview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepageview, name='homepage') # This is the line that tells Django to look for the urls.py file in the homepage app
    
]
