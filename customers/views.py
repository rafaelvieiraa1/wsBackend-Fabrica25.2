from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from customers.models import Customer
from django.urls import reverse_lazy

class CustomerListView(ListView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['cnpj', 'company_name', 'phone', 'email']

class CustomerDetailView(DetailView):
    model = Customer

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['cnpj', 'company_name', 'phone', 'email']

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')
    