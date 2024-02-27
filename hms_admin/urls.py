from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='adim-home'),
    path('room/',views.room,name='admin-room'),
    
]
