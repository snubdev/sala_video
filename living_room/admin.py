from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'video')
    prepopulated_fields = {'slug': ('title',)}