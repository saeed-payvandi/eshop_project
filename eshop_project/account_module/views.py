from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from .models import User
from django.utils.crypto import get_random_string
from django.urls import reverse
# from django.contrib.auth import get_user_model

# Create your views here.

# user = get_user_model()


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email, 
                    username=user_email, 
                    is_active=False, 
                    email_active_code=get_random_string(72))
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                return redirect(reverse('login_page'))




        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/register.html', context)
    

class LoginView(View):
    def get(self, request):
        context = {
            'login_form': None,
        }
        return render(request,'account_module/register.html', context)

    def post(self, request):
        pass

