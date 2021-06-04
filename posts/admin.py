from django.contrib import admin
from .models import Blogs, Author, Entry
from profiles_api import models
# Register your models here.
admin.site.register(Blogs)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(models.UserProfile)
