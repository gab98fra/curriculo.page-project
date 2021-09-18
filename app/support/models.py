from django.db import models
from django.contrib.auth.models import User


class FAQModel(models.Model):
    "FAQ Model"
    
    id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=100)
    answer=models.TextField(max_length=500)
    image=models.ImageField(upload_to='PF/%y/%m/%d', null=True, blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)


class AssistanceModel(models.Model):
    "Assistance Model"
    
    id=models.AutoField(primary_key=True)
    issue=models.CharField(max_length=40)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=True)#Activo o cerrado
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class FeedbackModel(models.Model):
    "Feedback model"
    
    id=models.AutoField(primary_key=True)
    issue=models.CharField(max_length=40)
    description=models.TextField(max_length=500)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
