# from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from account_module.models import User
# from django.utils.text import slugify


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'{self.title} - {self.url_title}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


# class ProductInformation(models.Model):
#     color = models.CharField(max_length=200, verbose_name='رنگ')
#     size = models.CharField(max_length=200, verbose_name='سایز')
#
#     def __str__(self):
#         return f'{self.size} - {self.color}'
#
#     class Meta:
#         verbose_name = 'اطلاعات تکمیلی'
#         verbose_name_plural = 'تمامی اطلاعات تکمیلی'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    # product_information = models.OneToOneField(
    #     ProductInformation,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     related_name='product_information',
    #     verbose_name='اطلاعات تکمیلی'
    #     ,blank=True)

    # category = models.ForeignKey(
    #     ProductCategory,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     related_name='products',
    #     verbose_name='دسته بندی')
    brand = models.ForeignKey(
        ProductBrand,
        on_delete=models.CASCADE,
        verbose_name='برند',
        null=True,
        blank=True)
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    # product_tags = models.ManyToManyField(ProductTag, verbose_name='تگ های محصول')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر مجصول')
    price = models.IntegerField(verbose_name='قیمت')
    # rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(max_length=200, default="", null=False, blank=True, unique=True, verbose_name='عنوان در url')  # default=> db_index=True & max_length=50
    # slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title + ' id ' + self.id)
        # super().save(*args, **kwargs)  # for generate id to save in slug
        # self.slug = slugify(f"{self.title} id {self.id}")
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    
    def __str__(self):
        return f'{self.product.title} / {self.ip}'
    
    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'
