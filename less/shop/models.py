from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField#AutoField is used to keep unique ids read about them in django documentation @ https://docs.djangoproject.com/en/5.1/
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    publish_date=models.DateField()