from django.contrib import admin

# Register your models here.
from Pentagram.models import Photo
from Pentagram.models import Comment, Like

admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Like)