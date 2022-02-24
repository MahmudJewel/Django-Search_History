from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateField(auto_now_add=True)
    result = models.CharField(max_length=200, blank=True, null=True)
    
    
