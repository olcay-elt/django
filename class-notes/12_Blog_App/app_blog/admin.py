from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(BlogComment)