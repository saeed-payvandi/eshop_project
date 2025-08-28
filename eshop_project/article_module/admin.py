from django.contrib import admin
from django.http import HttpRequest
from .models import ArticleCategory, Article, ArticleComment

# Register your models here.


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        # print('change: ', change)
        # print('request: ', request)
        # print('user: ', request.user)
        # print('object:', obj)
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'parent']


