from django.db import models
from manage_accounts.models import MyUser


# Create your models here.
class Video(models.Model):
    video=models.FileField(upload_to='app/student/video',null=True)
    video_name=models.CharField(max_length=150,blank=True)
    
    
class Image(models.Model):
    image=models.ImageField(upload_to='app/student/image',null=True)
    image_name=models.CharField(max_length=150,blank=True)
    
class Link(models.Model):
    link_name=models.TextField()
    link_desc=models.TextField(blank=True,null=True)
    update_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    subject=models.ForeignKey("Subject",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.link_name
    
    
class Topic(models.Model):
    topic_name=models.TextField()
    links=models.ManyToManyField(Link,related_name="topic_link")
    images=models.ManyToManyField(Image,on_delete=models.CASCADE)
    videos=models.ManyToManyField(Video,on_delete=models.CASCADE)
    update_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.topic_name    






class Unit(models.Model):
    name=models.CharField(max_length=120)
    topics=models.ManyToManyField(Topic,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name   
    
class Subject(models.Model):
    units=models.ManyToManyField(Unit,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    subject_status=models.IntegerField(blank=True,null=True)
    img=models.ImageField(uploaded_to="app/subjects/img",null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
   
    def __str__(self) -> str:
        return self.name 
   
class StudentChat(models.Model):
    student_name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    message=models.TextField()
    chat_img=models.ImageField(upload_to="app/students/chat_images",null=True,blank=True)
    chat_doc=models.FileField(upload_to="app/students/chat_docs",null=True,blank=True)
    
    def __str__(self) -> str:
        return '%s-%s' % (self.student_name.first_name,self.student_name.last_name)
    class Meta:
        ordering=["-pub_date"]
    
class FacultyChat(models.Model):
    faculty_name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    message=models.TextField()
    chat_img=models.ImageField(upload_to="app/faculty/chat_images",null=True,blank=True)
    chat_doc=models.FileField(upload_to="app/faculty/chat_docs",null=True,blank=True)
    
    def __str__(self) -> str:
        return '%s-%s' % (self.faculty.first_name,self.faculty.last_name)
    class Meta:
        ordering=["-pub_date"]
     
     
     
     
class Quiz(models.Models):
    question=models.TextField()
    option_A=models.TextField()
    option_B=models.TextField()
    option_C=models.TextField(null=True,blank=True)
    option_D=models.TextField(null=True,blank=True)
    right=models.BooleanField(null=True,default=False)
    wrong=models.BooleanField(null=True,default=False)
    
    def __str__(self) -> str:
        return self.question
    class Meta:
        ordering=["-pub_date"]
    
class ClassActivity(models.Model):
   all_chats=models.ManyToManyField(StudentChat,on_delete=models.CASCADE)
   student_name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
   topics=models.ManyToManyField(Topic,null=True,blank=True,on_delete=models.CASCADE)
   links=models.ManyToManyField(Link,null=True,blank=True,on_delete=models.CASCADE)
   
     