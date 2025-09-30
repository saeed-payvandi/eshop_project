from django.shortcuts import render
from django.http import HttpRequest
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from .forms import EditProfileModelForm

# Create your views here.


class UserPanelDashboardPage(TemplateView):
    template_name = 'User_panel_module/user_panel_dashboard_page.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        # edit_form = EditProfileModelForm(initial={
        #     'first_name': current_user.first_name,
        #     'last_name': current_user.last_name,
        # })
        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')
