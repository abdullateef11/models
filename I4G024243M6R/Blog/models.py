from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class post(models.Model):

    Title=models.CharField(max_length=200)
    Text=models.TextField(max_length=1000)
    Author=models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date=models.DateTimeField()
    Published_Date=models.DateTimeField()