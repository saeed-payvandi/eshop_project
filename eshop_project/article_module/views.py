from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Article
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['date'] = datetime2jalali(self.request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    #     # context['date'] = datetime2jalali(self.request.user.date_joined)
    #     context['date'] = date2jalali(self.request.user.date_joined)
    #     return context