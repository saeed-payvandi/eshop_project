from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


# admin.site.register(models.SiteSetting)
# admin.site.register(models.FooterLinkBox)
# admin.site.register(models.FooterLink, FooterLinkAdmin)
