from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
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
            print(register_form.cleaned_data)
            # todo: register user
            pass

        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/register.html', context)

