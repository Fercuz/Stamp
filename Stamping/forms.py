from django import forms

class Formulario (forms.Form):
    email = forms.EmailField(label='')
    nombre = forms. CharField(label='',max_length=100)
    mensaje =  forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))
