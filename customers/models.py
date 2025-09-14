
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class Customer(models.Model):
    """
    Model representing a customer/client
    """
    cnpj = models.CharField(
        max_length=18,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
                message='CNPJ must be in format XX.XXX.XXX/XXXX-XX'
            )
        ],
        help_text='CNPJ in format XX.XXX.XXX/XXXX-XX'
    )
    company_name = models.CharField(
        max_length=255,
        help_text='Legal company name (Razão Social)'
    )
    phone = models.CharField(
        max_length=20, 
    )
    email = models.EmailField(
        max_length=254,
        help_text='Customer email address'
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return f"{self.company_name} ({self.cnpj})"
    
    def get_absolute_url(self):
        return reverse('customer_detail', args=[self.id])
