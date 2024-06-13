from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name =
    last_name =
    phone =
    email =
    password =

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Product(models.Model):

class Order(models.Model):
