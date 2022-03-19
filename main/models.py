from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'client'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Slider(models.Model):
    img = models.ImageField(upload_to="Slider/")
    title  = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

class Categories(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="Categories/")

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Product/")
    price = models.IntegerField()
    
class Info(models.Model):
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    map =  models.CharField(max_length=200)

class Newsletters(models.Model):
    email = models.EmailField()

class Blog(models.Model):
    img = models.ImageField(upload_to="Blog/")
    title  = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

class About(models.Model):
    img = models.ImageField(upload_to="About/")
    text1 = models.CharField(max_length=200)
    text2 = models.CharField(max_length=200)

class Contact(models.Model):
    email = models.EmailField()
    msg = models.CharField(max_length=255)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
