from django import forms

class UploadFileForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    arquivo = forms.FileField()