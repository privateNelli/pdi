from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('casos', views.caso, name='casos')
]
