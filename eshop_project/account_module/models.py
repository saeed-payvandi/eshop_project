from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    # mobile = models.CharField(max_length=20, verbose_name='تلفن همراه', null=True)


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()


# class UserProfile(models.Model):
#     pass
