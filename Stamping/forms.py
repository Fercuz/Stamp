from django import forms

class Contacto_Form (forms.Form):
    email = forms.EmailField(label='',widget=forms.Textarea(attrs={'placeholder': 'Email'}))
    titulo = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Asunto'}),max_length=100)
    texto =  forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))

class Factura_Form (forms.Form):
    codigo_factura = forms.CharField(widget=forms.TextInput())
    nombre_cliente = forms.CharField(widget=forms.TextInput())
    apellido_cliente = forms.CharField(widget=forms.TextInput())
    nombre_empleado = forms.CharField(widget=forms.TextInput())
    fecha = forms.CharField(widget=forms.TextInput())
    total = forms.CharField(widget=forms.TextInput())

    def clean(self):
    	return self.cleaned_data
