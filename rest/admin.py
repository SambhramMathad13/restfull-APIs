from django.contrib import admin
from .models import Studs

class StudsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll') 

admin.site.register(Studs, StudsAdmin)

