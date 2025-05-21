from django.db import models

# Create your models here.
from django.db import models

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.product_id})"
    
class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.customer_name} ({self.customer_id})"

from django.db import models

class Order(models.Model):
    customer_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=50)
    delivery_address = models.TextField()
    mode_of_transaction = models.CharField(max_length=50)

    def __str__(self):
        return f"Order by Customer {self.customer_id} for Product {self.product_id}"

