from django.contrib import admin
from .models import bhagtan

# Register your models here.
class myteam(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "age", "singer") 

admin.site.register(bhagtan, myteam)