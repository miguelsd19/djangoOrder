from django.contrib import admin
from season.models import Season

# Register your models here.
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'date']