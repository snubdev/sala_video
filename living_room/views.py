from django.shortcuts import render, get_object_or_404
from .models import Room


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'post/list.html', {'rooms': rooms})


def room_detail(request, year, month, day, room):
    room = get_object_or_404(Room, slug=room,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'post/detail.html', {'room': room})
