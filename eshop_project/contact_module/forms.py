from django import forms


class ContactUsForms(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی')
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField()
    # text = forms.CharField(widget=forms.Textarea)

