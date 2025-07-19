from django import forms
from .models import ContactUs 


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        # required=False,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی',
        }))
    email = forms.EmailField(
        label='ایمیل', 
        # required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل',
        }))
    title = forms.CharField(
        label='عنوان',
        # required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان',
        }))
    message = forms.CharField(
        label='متن پیام', 
        # required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message',
            'rows': '5',
            'placeholder': 'متن پیام',
        }))
    

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'row': '5',
                'id': 'message',
            }),
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری میباشد. لطفا وارد کنید',
            },
        }