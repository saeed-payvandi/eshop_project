from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory, ArticleComment
from django.http import HttpRequest, HttpResponse
from jalali_date import datetime2jalali, date2jalali

# Create your views here.


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles': articles
#         }
#         return render(request, 'article_module/articles_page.html', context)


class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        # print(self.kwargs)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['date'] = datetime2jalali(self.request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    #     # context['date'] = datetime2jalali(self.request.user.date_joined)
    #     context['date'] = date2jalali(self.request.user.date_joined)
    #     return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article: Article = kwargs.get('object')
        # print('kwargs:', kwargs)
        # print('object:', self.object.pk)
        # article = kwargs['object']
        # print(article)
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent=None).order_by('-create_date').prefetch_related('articlecomment_set')
        return context


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        'main_categories': article_main_categories,
    }
    return render(request, 'article_module/components/article_categories_components.html', context)


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        # print(article_id, article_comment, parent_id)
        new_comment = ArticleComment(article_id=article_id, text=article_comment, user_id=request.user.id, parent_id=parent_id)
        new_comment.save()
    # print(request.GET)
    return HttpResponse('response')
