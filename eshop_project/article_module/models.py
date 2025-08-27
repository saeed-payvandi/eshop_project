from django.db import models
from account_module.models import User
from jalali_date import datetime2jalali, date2jalali


# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE, verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسنه بندی های مقاله'


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان در مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    selected_categories = models.ManyToManyField(to=ArticleCategory, verbose_name='دسنه بندی ها')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, editable=False, verbose_name='نویسنده')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.title
    
    def get_jalali_create_date(self):
        return date2jalali(self.create_date)
    
    def get_jalali_create_time(self):
        return self.create_date.strftime("%H:%M")

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'


