from django.contrib import admin
from .models import Topic, Recipe

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Topic)

