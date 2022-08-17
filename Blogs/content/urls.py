from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, loginPage, signUpPage, logoutPage


urlpatterns = [
    path('signup/', signUpPage),
    path('login/', loginPage),  
    path('logout/', logoutPage),
    
    path('', home),
    path('content/<slug:url>/', post)
]
