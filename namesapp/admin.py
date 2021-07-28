from django.contrib import admin

# Register your models here.

from .models import NYCAlready, NYCCurrent

admin.site.register(NYCAlready)
admin.site.register(NYCCurrent)
