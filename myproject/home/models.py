from django.db import models
 


# Create your models here.
class Details(models.Model):
    sr_no=models.IntegerField()
    emp_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=255)
    department=models.CharField(max_length=200)
    salary=models.IntegerField()
    role=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    date=models.DateField()
