from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Caption)
admin.site.register(Comment)
admin.site.register(Follow)
