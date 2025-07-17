from django import forms


class ContactUsForms(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        # required=False,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
        }
        )
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput)
    subject = forms.CharField(label='عنوان')
    text = forms.CharField(label='متن پیام', widget=forms.Textarea)
    # text = forms.CharField(widget=forms.Textarea)

