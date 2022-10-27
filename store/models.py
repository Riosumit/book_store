from distutils.command.upload import upload
import email
from unicodedata import category
from django.db import models

# Create your models here.
class books(models.Model):
    id = models.AutoField
    book_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    Author = models.CharField(max_length=50, default="")
    Publication = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    discount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=400)
    pub_date = models.DateField()
    quantity = models.IntegerField(default=0)
    rating = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to="store/images")

    def __str__(self):
        return self.book_name

class user(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()
    contact = models.IntegerField(default=0)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name