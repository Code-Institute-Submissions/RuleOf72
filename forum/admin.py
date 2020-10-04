from django.contrib import admin
from .models import Forum_topic, Forum_comment
# Register your models here.

admin.site.register(Forum_topic)
admin.site.register(Forum_comment)
