from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

class HowMatchProducts(forms.Form):
    text = forms.IntegerField()
    text1 = forms.IntegerField()

