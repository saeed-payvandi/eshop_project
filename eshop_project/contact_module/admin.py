from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass

# admin.site.register(models.ContactUs)
