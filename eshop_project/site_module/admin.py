from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    pass


# admin.site.register(models.SiteSetting, SiteSettingAdmin)
