from django.contrib import admin

# Register your models here.

from .models import UserProfile, Song, Album, Relationship
admin.site.register(UserProfile)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Relationship)
