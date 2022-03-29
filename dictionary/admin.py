from django.contrib import admin
from .models import Dictionary


# Register your models here.

class DictAdmin(admin.ModelAdmin):
    list_display = ['inglizcha', 'ozbekcha']


admin.site.register(Dictionary, DictAdmin)
