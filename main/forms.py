from django import forms


class EmailPostForm(forms.Form):
    formEmail = forms.EmailField()
    formTheme = forms.CharField(max_length=36)
    formMessage = forms.CharField(max_length=250)
    formFile = forms.ImageField(required=False)
