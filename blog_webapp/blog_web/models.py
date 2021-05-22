from django.db import models
class destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField
    offer=models.BooleanField(default=False)

# Create your models here.
class Create_article(models.Model):
    username=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    private= models.BooleanField(default=False)