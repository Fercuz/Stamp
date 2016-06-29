from django import forms

class Formulario (forms.Form):
    email = forms.EmailField(label='',widget=forms.Textarea(attrs={'placeholder': 'Email'}))
    titulo = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Asunto'}),max_length=100)
    texto =  forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))


# class Formulario (forms.Form):
#     email = forms.EmailField(label='',widget=forms.Textarea(attrs={'placeholder': 'Email'}))
#     asunto = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Asunto'}),max_length=100)
#     mensaje =  forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))
