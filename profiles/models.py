from django.db import models
from manage_accounts.models import MyUser
from contents.models import Subject,StudentChat,Video
# Create your models here.
class Student(models.Model):
    student=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    score=models.IntegerField(max_length=100,blank=True)
    chat_activities=models.ManyToManyField(StudentChat,blank=True,on_delete=models.CASCADE)
    recent_lectures=models.ManyToManyField(Video,blank=True,on_delete=models.CASCADE)
    
class Faculty(models.Model):
    faculty=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,blank=True,on_delete=models.CASCADE)
    