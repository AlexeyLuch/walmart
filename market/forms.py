from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()



# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
