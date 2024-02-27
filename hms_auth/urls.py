from django.urls import path

from . import views

urlpatterns = [
    path('login_register/',views.login_registerView,name='login_register'),
    path('login/',views.loginView,name='login'),
    path('register/',views.registerVIew,name='register'),
    path('logout/',views.logoutView,name='logout')
]
