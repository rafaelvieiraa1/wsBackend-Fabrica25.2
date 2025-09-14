from django.db import models
from customers.models import Customer

class Manufacturer(models.TextChoices):
    ELGIN = 'ELGIN', 'Elgin'
    EPSON = 'EPSON', 'Epson'
    BEMATECH = 'BEMATECH', 'Bematech'

class Device(models.Model):
    """
    Model representing a printer/device
    """
    model = models.CharField(
        max_length=100,
        help_text='Device model name'
    )
    manufacturer = models.CharField(
        max_length=100,
        help_text='Device manufacturer'
    )
    serial_number = models.CharField(
        max_length=100,
        unique=True,
        help_text='Device serial number'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='devices',
        help_text='Customer who owns this device'
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
    
    def __str__(self):
        return f"{self.manufacturer} {self.model} (S/N: {self.serial_number})"