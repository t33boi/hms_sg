from django.shortcuts import render,redirect

# Create your views here.

from .models import Person,Room,BookRoom

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')

def room(request):
    rooms = Room.objects.all()
    context = {
        'rooms' : rooms,
        
    }
    return render(request,'room.html',context)

def book_room(request,pk):
    room_booked = Room.objects.get(id=pk)
    booked_room = BookRoom.objects.create(user=request.user,room=room_booked)
    booked_room.save()
    return redirect('check_out')

def check_out(request):
    user = request.user 
    user = Person.objects.get(username=user)
    user_room = user.bookroom_set.all()
    print(user_room)
    context = {
        'rooms' : user_room,
}
    return render(request,'check_out.html',context)

def check_out_delete(request,pk):
    user = request.user 
    user = Person.objects.get(username=user)
    user_room = user.bookroom_set.get(id=pk)
    user_room.delete()
    return redirect('check_out')
