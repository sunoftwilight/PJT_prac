from django.contrib import admin
from .models import Board, Comment

# Register your models here.
admin.site.register([Board, Comment])