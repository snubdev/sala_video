from django.shortcuts import render, get_object_or_404
from .models import Room
from .forms import RoomForm


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'post/list.html', {'rooms': rooms})


def room_detail(request, year, month, day, room):
    room = get_object_or_404(Room, slug=room,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'post/detail.html', {'room': room})


def create_room(request):
    if request.method == 'POST':
        room_form = RoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
    else:
        room_form = RoomForm()

    return render(request, 'post/create_room.html', {'room_form': room_form})
