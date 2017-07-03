from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.ForeignKey(User,related_name='products')
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,null=False)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0)

    def __str__(self):
        return self.name


class Order(models.Model):

    Status = (
        ('c', 'Cancelled'),
        ('p', 'Pending'),
        ('s', 'Shipped'),
        ('a', 'Arrived'),
    )
    owner = models.ForeignKey(User, related_name='orders')
    total = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    products = models.ManyToManyField(Product)
    status = models.CharField(max_length=2,choices=Status,default='p')
    create_time = models.DateTimeField(default=now())
    update_time = models.DateTimeField(blank=True,null=True)


class Cart(models.Model):
    owner = models.ForeignKey(User,unique=True,null=False,blank=False)
    total = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    products = models.ManyToManyField(Product,blank=True,null=False)

    def __str__(self):
        return self.owner.username
