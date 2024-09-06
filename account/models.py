from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey

class User(AbstractUser):
    STATUS = (
        ('admin', 'Admin'),
        ('user', 'User')     
    )
    phone = models.CharField(max_length=14,)
    photo = models.ImageField(upload_to='Users/', default='1.png')
    status = models.CharField(max_length=50, choices=STATUS, default='User')

    def __str__(self):
        return f'{self.first_name}/{self.status}'

# ---------------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    photo = models.ImageField(upload_to='Category_ph/')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

# --------------------------------------------------------------------------------------

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    batafsil = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Product_Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_images/',  null=True, blank=True)



#-------------------------------------------------------------------------------------
# class Savat(models.Model):
    

# Create your models here.