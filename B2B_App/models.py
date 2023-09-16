from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Customer_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phonenumber = models.CharField(max_length=100,null=True)


class Farmer_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phonenumber = models.CharField(max_length=100,null=True)



class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='images/', null=True)
    desc=models.TextField(null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    auction_date=models.CharField(max_length=100,null=True)
    delivery_date=models.CharField(max_length=100,null=True)
    farmer = models.ForeignKey(Farmer_Reg, on_delete=models.CASCADE,null=True)


class chat(models.Model):
    message = models.CharField(max_length=250, null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    farmer = models.ForeignKey(Farmer_Reg, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=250, null=True)
    reply = models.CharField(max_length=250, null=True)

class Auction(models.Model):
    price = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer_Reg, on_delete=models.CASCADE, null=True)
    farmer = models.ForeignKey(Farmer_Reg, on_delete=models.CASCADE, null=True)
    status=models.CharField(max_length=100,null=True)
    product_name=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=100,null=True)
    admin_status=models.CharField(max_length=100,null=True)

class fixed_auction(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=100,null=True)
    price=models.CharField(max_length=100,null=True)
    Auction_price=models.CharField(max_length=100,null=True)
    payment=models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    customer = models.ForeignKey(Customer_Reg, on_delete=models.CASCADE, null=True)
    farmer = models.ForeignKey(Farmer_Reg, on_delete=models.CASCADE, null=True)
    com_date=models.DateField(null=False, blank=False, auto_now=True)



