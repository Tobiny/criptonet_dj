from importlib._common import _

from django import forms
from django.core.exceptions import ValidationError


class AddProductosForm(forms.Form):
    mod_modelo = forms.CharField(help_text="Ingrese el nuevo modelo")

    def clean_mod_modelo(self):
        data = self.cleaned_data['mod_modelo']

        if str(data):
            raise ValidationError(_('Formulario inválido - campo vacío'))
        return data

