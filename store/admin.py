from django.contrib import admin

# Register your models here.
from .models import books, user

admin.site.register(books)
admin.site.register(user)