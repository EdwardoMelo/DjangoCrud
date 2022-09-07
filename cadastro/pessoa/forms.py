from django import forms
from .models import Pessoa, Contato
from django.forms import fields, models


class DateInput(forms.DateInput):
    input_type = 'date'


class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=DateInput)

    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativa']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']