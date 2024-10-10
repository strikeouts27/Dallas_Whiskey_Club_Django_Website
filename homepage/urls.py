#Dallas_Whiskey_Club_Django_Website/
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')), # This is the line that tells Django to look for the urls.py file in the homepage app
]
