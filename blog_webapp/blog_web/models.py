from django.db import models

# Create your models here.
class Create_article(models.Model):
    username=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/')
    private= models.BooleanField(default=False)

class register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    confirm_password= models.CharField(max_length=20)
