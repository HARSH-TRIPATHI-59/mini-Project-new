from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.Logout, name='logout'),
    path('index', views.indes, name='index-1'),
    path('main', views.main, name='main'),
    path('about', views.about, name='about'),
    path('option', views.option, name='option'),
    path('contactus', views.contactus, name='contactus')

]

