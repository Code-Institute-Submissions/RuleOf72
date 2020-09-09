from django.contrib import admin
from .models import ForumTopic, ForumComments
# Register your models here.

admin.site.register(ForumTopic)
admin.site.register(ForumComments)