from django.urls import reverse_lazy
from customers.models import Customer
from customers.forms import CustomerForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView



class CustomerListView(ListView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm

class CustomerDetailView(DetailView):
    model = Customer

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')
    