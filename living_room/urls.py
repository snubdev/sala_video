from django.urls import path
from . import views

app_name = 'living_room'

urlpatterns = [
    path('',  views.room_list, name='room_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:room>/', views.room_detail, name='room_detail')
]