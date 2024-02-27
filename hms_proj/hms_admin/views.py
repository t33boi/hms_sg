from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'admin.html')

def room(request):
    return render(request,'admin-room.html')