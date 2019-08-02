from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from datetime import datetime
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 50)
    
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    email = models.EmailField(default = "")
    address = models.CharField(max_length = 500) 
    staff_id = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    registration_date = models.DateTimeField(default = timezone.now)
    resumption_date = models.DateField(default = datetime.today)
    status = models.CharField(max_length = 3, default = "No")
