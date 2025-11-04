from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView
from article_module.models import Article

# Create your views here.


def index(request: HttpRequest):
    return render(request, 'admin_panel/home/index.html')


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


class ArticleEditView(UpdateView):
    model = Article
    template_name = 'admin_panel/articles/edit_article.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_articles')
    # success_url = '/admin-panel/articles/'
