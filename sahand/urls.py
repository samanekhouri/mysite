
from django.urls import path
from sahand.views import* 

urlpatterns = [
     path('home',index_view),
     path('abaut',about_view),
     path('contact',contact_view) ,  

       ]
    