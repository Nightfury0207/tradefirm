from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    address = models.TextField(max_length=254)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    client_gstn = models.CharField(max_length=15)
    remark = models.TextField(max_length=100, blank=True)

class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_unit = models.CharField(max_length=20)
    item_opening_balance = models.IntegerField()
    item_hsn = models.CharField(max_length=10)
    item_gst_percent = models.IntegerField()

class Order_Parent(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_date = models.DateField()
    client_id = models.CharField(max_length=25)
    ordered_via = models.CharField(max_length=50)
    remark = models.TextField(max_length=100, blank=True)

class Order_Child(models.Model):
    order_id = models.CharField(max_length=25)
    item_id = models.CharField(max_length=25)
    quantity = models.IntegerField()
    remark = models.TextField(max_length=100, blank=True)

class Dispatch_Parent(models.Model):
    dispatch_id = models.BigAutoField(primary_key=True)
    order_id = models.CharField(max_length=25)
    remark = models.TextField(max_length=100, blank=True)

class Dispatch_Child(models.Model):
    dispatch_id = models.CharField(max_length=25)
    dispatc_date = models.DateField()
    item_id = models.CharField(max_length=25)
    quantity = models.IntegerField()
    remark = models.TextField(max_length=100, blank=True)

class Inward_Parent(models.Model):
    inward_id = models.BigAutoField(primary_key=True)
    inward_date = models.DateField()
    remark = models.TextField(max_length=100, blank=True)

class Inward_Child(models.Model):
    inward_id = models.CharField(max_length=25)
    item_id = models.CharField(max_length=25)
    quantity = models.IntegerField()
    remark = models.TextField(max_length=100, blank=True)