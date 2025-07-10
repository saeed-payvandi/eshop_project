from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class ProductTag(models.Model):
    tag = models.CharField(max_length=300, verbose_name='عنوان')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return f'{self.title} - {self.url_title}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='رنگ')
    size = models.CharField(max_length=200, verbose_name='سایز')

    def __str__(self):
        return f'{self.size} - {self.color}'

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = 'تمامی اطلاعات تکمیلی'


class Product(models.Model):
    title = models.CharField(max_length=300)
    product_information = models.OneToOneField(
        ProductInformation,
        on_delete=models.CASCADE,
        null=True,
        related_name='product_information',
        verbose_name='اطلاعات تکمیلی'
        ,blank=True)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='products',
        verbose_name='دسته بندی')
    product_tags = models.ManyToManyField(ProductTag, verbose_name='تگ های محصول')
    price = models.IntegerField(verbose_name='قیمت')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    # slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        # self.slug = slugify(self.title + ' id ' + self.id)
        super().save(*args, **kwargs)  # for generate id to save in slug
        self.slug = slugify(f"{self.title} id {self.id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
