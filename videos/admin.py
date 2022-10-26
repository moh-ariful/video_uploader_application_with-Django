from django.contrib import admin
from videos.models import Category, Video, Comment


admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Comment)