from django import forms
from Stamping.models import *
from datetime import date


class Contacto_Form (forms.Form):
    email = forms.EmailField(label='',widget=forms.Textarea(attrs={'placeholder': 'Email'}))
    titulo = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Asunto'}),max_length=100)
    texto =  forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))

class Venta_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Venta_Form, self).__init__(*args, **kwargs)
        # Para cambiar el valor de un campo
        self.fields['vendedor'].initial = "Administrador"

    class Meta:
        model = Venta
        fields = '__all__'

class Compra_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Compra_Form, self).__init__(*args, **kwargs)
        # Para cambiar el valor de un campo
        self.fields['comprador'].initial = "Administrador"

    class Meta:
        model = Compra
        fields = '__all__'