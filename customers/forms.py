from django import forms
from customers.models import Customer
import requests
import re
from django.conf import settings

class CNPJClient:
    API_URL = settings.CNPJ_API_URL
    def get(self, cnpj):
        response = requests.get(self.API_URL + cnpj)
        if response.status_code == 200:
            return response.json()
        return None

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cnpj']
    
    def __init__(self, *args, **kwargs):
        self.client = CNPJClient()
        self.cnpj_data = None
        super().__init__(*args, **kwargs)

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        cnpj_numbers = re.sub(r'\D', '', cnpj)  # Remove non-numeric characters
        data = self.client.get(cnpj_numbers)
        if not data: 
            raise forms.ValidationError("CNPJ not found")
        self.cnpj_data = data
        return cnpj

    def save(self, commit=True):
        self.instance.company_name = self.cnpj_data['razao_social']   
        self.instance.email = self.cnpj_data['estabelecimento']['email']
        phone = self.cnpj_data['estabelecimento']['ddd1'] + self.cnpj_data['estabelecimento']['telefone1']
        self.instance.phone = phone
        return super().save(commit)
       