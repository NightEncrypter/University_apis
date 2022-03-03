from django.db import models

# Create your models here.
class Video(models.Model):
    video=models.FileField(upload_to='student/video',null=True)
    video_name=models.CharField(max_length=250,blank=True)