from django.db import models

# Create your models here.

#Our Customer's content
class Customer(models.Model):
    name= models.CharField(max_length=200,null=True)
    phone= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    date= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

#Our Product content
class Product(models.Model):
    CATEGORY = (
        ("Small","Small"),
        ("Medium", "Medium"),
        ("Large", "Large")
    )
    name= models.CharField(max_length=200,null=True)
    price= models.FloatField(null=True)
    category= models.CharField(max_length=200,null=True)
    date= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
