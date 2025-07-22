from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse
from .models import ContactUs, UserProfile


# Create your views here.


class ContactUsView(CreateView):
    # model = ContactUs
    # fields = ['']
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'


# def store_file(file):
#     with open('temp/image.jpg', 'wb+') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'contact_module/create_profile_page.html', {
#             'form': form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#             # store_file(request.FILES['user_image'])
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return redirect('/contact-us/create-profile')
#
#         return render(request, 'contact_module/create_profile_page.html', {
#             'form': submitted_form
#         })


# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form,
#         })
#
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
#
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })


# def contact_us_page(request):
#     # if request.method == 'POST':
#     #     entered_email = request.POST['email']
#     #     if entered_email == '':
#     #         return render(request, 'contact_module/contact_us_page.html', {
#     #             'has_error': True,
#     #         })
#     #     print(request.POST['email'])
#     #     print(request.POST['fullname'])
#     #     print(request.POST['subject'])
#     #     print(request.POST['message'])
#     #     return redirect(reverse('home_page'))
#
#     # contact_form = ContactUsForms(request.POST or None)
#
#     if request.method == 'POST':
#         # contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             # print(contact_form.cleaned_data)
#             # contact = ContactUs(
#             #     title=contact_form.cleaned_data.get('title'),
#             #     email=contact_form.cleaned_data.get('email'),
#             #     full_name=contact_form.cleaned_data.get('full_name'),
#             #     message=contact_form.cleaned_data.get('message'),
#             #     # is_read_by_admin=False,
#             # )
#             # contact.save()
#             contact_form.save()
#             return redirect('home_page')
#     else:
#         # contact_form = ContactUsForm()
#         contact_form = ContactUsModelForm()
#
#     return render(request, 'contact_module/contact_us_page.html', {
#         # 'has_error': False,
#         'contact_form': contact_form,
#     })
