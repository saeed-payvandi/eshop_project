from django.contrib import admin
from .models import ArticleCategory, Article

# Register your models here.


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass



