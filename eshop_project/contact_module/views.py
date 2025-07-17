from django.shortcuts import render, redirect
# from django.urls import reverse
from .forms import ContactUsForms


# Create your views here.


def contact_us_page(request):
    # if request.method == 'POST':
    #     entered_email = request.POST['email']
    #     if entered_email == '':
    #         return render(request, 'contact_module/contact_us_page.html', {
    #             'has_error': True,
    #         })
    #     print(request.POST['email'])
    #     print(request.POST['fullname'])
    #     print(request.POST['subject'])
    #     print(request.POST['message'])
    #     return redirect(reverse('home_page'))

    # contact_form = ContactUsForms(request.POST or None)
    
    if request.method == 'POST':
        contact_form = ContactUsForms(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect('home_page')
    else:
        contact_form = ContactUsForms()

    return render(request, 'contact_module/contact_us_page.html', {
        # 'has_error': False,
        'contact_form': contact_form,
    })
