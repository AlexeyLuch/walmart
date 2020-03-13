from django import forms

from .models import contact


class UploadFileForm(forms.Form):
    file = forms.FileField()

class HowMatchProducts(forms.Form):
    text = forms.CharField()

