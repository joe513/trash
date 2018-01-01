from django.contrib import admin
from first.models import Sites


class MyAdminModel(admin.ModelAdmin):

    list_display = ['name', 'url']


admin.site.register(Sites, MyAdminModel)
