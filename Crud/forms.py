from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Empresa,Cliente

class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['emp_cnpj','emp_razao_social','emp_email','emp_senha']

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cli_cpf','cli_nome','cli_email','cli_senha']