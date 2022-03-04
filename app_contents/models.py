from django.db import models

# Create your models here.
from django.db import models
from manage_accounts.models import MyUser
# from profiles.models import Faculty



class Student(models.Model):
    student_name=models.OneToOneField("MyUser",on_delete=models.CASCADE)
    score=models.IntegerField()
    chat_activities=models.ManyToManyField('StudentChat')
    recent_lectures=models.ManyToManyField('Video')
    recent_pdfs=models.ManyToManyField('Docx')
    recent_links=models.ManyToManyField('Link')
    batch=models.IntegerField(blank=True,null=True,max_length=10)
    performance=models.CharField(blank=True,null=True)
    
class Faculty(models.Model):
    faculty_name=models.OneToOneField("MyUser",on_delete=models.CASCADE,null=True,blank=True)
    subjects=models.ForeignKey('Subject',blank=True,null=True,on_delete=models.CASCADE)
    topics=models.ManyToManyField('Topic',blank=True,null=True)

# Create your models here.
class Video(models.Model):
    video=models.FileField(upload_to='app/student/videos',null=True)
    video_name=models.CharField(max_length=150,blank=True)
    
class Docx(models.Model):
    file=models.FileField(upload_to='app/student/files',null=True)
    file_name=models.CharField(max_length=150,blank=True)
    
    
class Image(models.Model):
    image=models.ImageField(upload_to='app/student/images',null=True)
    image_name=models.CharField(max_length=150,blank=True)
 
RELATED_LINKS=['TOPIC_LINKS','NORMAL','REDIRECT_LINK']   
class Link(models.Model):
    link_type=models.CharField(choices=RELATED_LINKS)
    link_name=models.TextField()
    link_desc=models.TextField(blank=True,null=True)
    update_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    subject=models.ForeignKey("Subject",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.link_name
    
    
class Topic(models.Model):
    topic_no=models.IntegerField(null=True)

    topic_name=models.TextField()
    links=models.ManyToManyField(Link)
    files=models.ManyToManyField(Docx)
    images=models.ManyToManyField(Image)
    videos=models.ManyToManyField(Video)
    update_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Topic {self.topic_no} {self.topic_name}" 






class Unit(models.Model):
    name=models.CharField(max_length=120)
    unit_no=models.IntegerField(null=True)
    topics=models.ManyToManyField(Topic)
    completed=models.BooleanField(null=True,default=False)
    def __str__(self) -> str:
        return f"Unit {self.unit_no} {self.name}"   
    
class Subject(models.Model):
    units=models.ManyToManyField(Unit)
    name=models.CharField(max_length=150)
    subject_status=models.IntegerField(blank=True,null=True)
    img=models.ImageField(upload_to="app/subjects/images",null=True,blank=True)
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

    
class FacultyChat(models.Model):
    faculty_name=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    message=models.TextField()
    chat_img=models.ImageField(upload_to="app/faculty/chat_images",null=True,blank=True)
    chat_doc=models.FileField(upload_to="app/faculty/chat_docs",null=True,blank=True)
    
    def __str__(self) -> str:
        return '%s-%s' % (self.faculty.first_name,self.faculty.last_name)

     
     
     
     
class Quiz(models.Model):
    question=models.TextField()
    option_A=models.TextField()
    option_B=models.TextField()
    option_C=models.TextField(null=True,blank=True)
    option_D=models.TextField(null=True,blank=True)
    right=models.BooleanField(null=True,default=False)
    wrong=models.BooleanField(null=True,default=False)
    
    def __str__(self) -> str:
        return self.question
   
    
class ClassActivity(models.Model):
   all_chats=models.ManyToManyField(StudentChat)
   student_name=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)
   topics=models.ManyToManyField(Topic)
   links=models.ManyToManyField(Link)
   

