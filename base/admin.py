from django.contrib import admin
from base.models import Movies

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','synopsis','cast')

admin.site.register(Movies, MovieAdmin)