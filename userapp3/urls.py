from django.urls import path

from userapp3 import views

urlpatterns = [
    path('', views.login, name='logout'),
    path('', views.logout, name='logout'),
    path('', views.signup, name='signup'),
    

]