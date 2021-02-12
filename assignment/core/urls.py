from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

   path('',views.home, name = "home" ),
   path('api/v1/calculate/',views.api_view,name = "api")
]
