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

        self.fields['vendedor'].initial = 'Julio Domingo'

        # Si ademas estamos editando un objeto propiedad
        if self.instance:
            # Podemos hacer lo que queramos
            ven = self.instance.vendedor


    def save(self, *args, **kwargs):      
        # Sobrecargar save devuelve el objeto apunto de ser guardado                   
        obj_propiedad = super(Venta_Form, self).save(*args, **kwargs)
 
        # Podemos hacer lo que queramos antes de guardarlo
        ven = obj_propiedad.vendedor
        try:
            # errror punto de partida
            obj_propiedad.save()
        except  AttributeError:
            return 'Lo sentimos!!..'
         
    def clean(self):
        # Sobrecargar clean devuelve un diccionario con los campos
        cleaned_data = super(Venta_Form, self).clean()
        ven = cleaned_data.get("vendedor")
 
        # if len(ven) < 3:
        #     # Podemos lanzar una excepcion que aparecera sobre el campo
        #     raise forms.ValidationError("Debe tener almenos 3 caracteres")
 
        # # Siempre hay que devolver el diccionario
        return cleaned_data
 
    class Meta:
            model = Venta
            fields = '__all__'
