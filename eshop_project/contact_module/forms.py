from django import forms


class ContactUsForms(forms.Form):
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
    subject = forms.CharField(
        label='عنوان',
        # required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان',
        }))
    text = forms.CharField(
        label='متن پیام', 
        # required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message',
            'rows': '5',
            'placeholder': 'متن پیام',
        }))