from django.contrib import admin
from .models import Hero, Category, Blog
# Register your models here.

admin.site.register(Hero)
admin.site.register(Category)
admin.site.register(Blog)