from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField#AutoField is used to keep unique ids read about them in django documentation @ https://docs.djangoproject.com/en/5.1/
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    desc=models.CharField(max_length=300)
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name