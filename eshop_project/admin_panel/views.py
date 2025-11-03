from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView
from article_module.models import Article

# Create your views here.


class ArticlesListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'admin_panel/articles/articles_list.html'

    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query