from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    #Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

#all of our products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

# class Order(models.Model):
