from django.contrib import admin
from .models import new

class Categori(admin.ModelAdmin):
    list_display = ("name", "number", "comment", "data",)

admin.site.register(new, Categori)