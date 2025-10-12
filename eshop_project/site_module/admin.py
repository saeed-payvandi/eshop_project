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


@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']


@admin.register(models.SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']


# admin.site.register(models.SiteSetting)
# admin.site.register(models.FooterLinkBox)
# admin.site.register(models.FooterLink, FooterLinkAdmin)
# admin.site.register(models.Slider, SliderAdmin)
# admin.site.register(models.SiteBanner, SiteBannerAdmin)
