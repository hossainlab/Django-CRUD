from django.contrib import admin
from .models import Developer 

class DeveloperAdmin(admin.ModelAdmin): 
    list_display = ['name', 'email', 'phone'] 
admin.site.register(Developer, DeveloperAdmin)