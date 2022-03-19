from email.policy import default
from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from manage_accounts.models import MyUser


# This is used FOR fACULTIES  ==> STUDENTS,FACULTIES
class Student(models.Model):
    student_name=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    score=models.IntegerField()
    chat_activities=models.ManyToManyField('StudentChat')
    recent_lectures=models.ManyToManyField('SubjectVideo')
    recent_pdfs=models.ManyToManyField('SubjectDocx')
    recent_links=models.ManyToManyField('Link')
    batch=models.IntegerField(blank=True,null=True)
    performance=models.CharField(blank=True,null=True,max_length=200)
   
   
# This is used FOR fACULTIES  ==> FACULTIES
class Faculty(models.Model):
    faculty_name=models.OneToOneField(MyUser,on_delete=models.CASCADE,null=True,blank=True)
    subjects=models.ForeignKey('Subject',blank=True,null=True,on_delete=models.CASCADE)
    topics=models.ManyToManyField('Topic')
    
    
# This is used for SUBJECT VIDEOS  ==> FACULTIES
class SubjectVideo(models.Model):
    video=models.FileField(upload_to='app/uploads/faculties/subjects/contents/videos',null=True)
    video_name=models.CharField(max_length=150,blank=True)
    
    def __str__(self) -> str:
        return f"{self.id} {self.video_name}"
    
# This is used for sUBJECT-dOCX  ==> FACULTIES    
class SubjectDocx(models.Model):
    file=models.FileField(upload_to='app/uploads/faculties/subjects/contents/files',null=True)
    file_name=models.CharField(max_length=150,blank=True)
    
    def __str__(self) -> str:
        return self.file_name
    
    
# This is used for sUBJECT-IMAGE  ==> FACULTIES
class SubjectImage(models.Model):
    image=models.ImageField(upload_to='app/uploads/faculties/subjects/contents/images',null=True)
    image_name=models.CharField(max_length=150,blank=True)
    def __str__(self) -> str:
        return self.image_name
RELATED_LINKS=(('TOPIC_LINKS','TOPIC_LINKS'),('NORMAL','NORMAL'),('REDIRECT_LINK','REDIRECT_LINK'))  

# This is used for all LINKS  ==> FACULTIES 
class Link(models.Model):
    link_type=models.CharField(choices=RELATED_LINKS,max_length=300)
    link_name=models.TextField()
    link_desc=models.TextField(blank=True,null=True)
    update_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    subject=models.ForeignKey("Subject",on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.link_name
    

# This is used for TOPICS  ==> FACULTIES
class Topic(models.Model):
    topic_no=models.IntegerField(null=True)

    topic_name=models.TextField()
    links=models.ManyToManyField(Link)
    files=models.ManyToManyField(SubjectDocx)
    images=models.ManyToManyField(SubjectImage)
    videos=models.ManyToManyField(SubjectVideo)
    update_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Topic {self.topic_no} {self.topic_name}" 





# This is used for UNIT ADDS  ==> FACULTIES

class Unit(models.Model):
    name=models.CharField(max_length=120)
    unit_no=models.IntegerField(null=True)
    topics=models.ManyToManyField(Topic)
    completed=models.BooleanField(null=True,default=False)
    def __str__(self) -> str:
        return f"Unit {self.unit_no} {self.name}"   
    
# This is used for Subject ADDS  ==> FACULTIES
class Subject(models.Model):
    units=models.ManyToManyField(Unit,blank=True)
    name=models.CharField(max_length=150)
    subject_status=models.IntegerField(blank=True,null=True)
    img=models.TextField(default='https://i.postimg.cc/vmM1Hnrc/books.jpg')
    desc=models.TextField(null=True,blank=True)
 
    
    def __str__(self) -> str:
        return self.name 

# This is used for CHATS  ==> STUDENTS
class StudentChat(models.Model):
    student_name=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    message=models.TextField()
    chat_img=models.ImageField(upload_to="app/chat_system/students/chat_images",null=True,blank=True)
    chat_doc=models.FileField(upload_to="app/chat_system/students/chat_docx",null=True,blank=True)
    
    def __str__(self) -> str:
        return '%s-%s' % (self.student_name.first_name,self.student_name.last_name)

# This is used for CHATS  ==> FACULTIES
class FacultyChat(models.Model):
    faculty_name=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    message=models.TextField()
    chat_img=models.ImageField(upload_to="app/chat_system/faculties/chat_images",null=True,blank=True)
    chat_doc=models.FileField(upload_to="app/chat_system/faculties/chat_docx",null=True,blank=True)
    
    def __str__(self) -> str:
        return '%s-%s' % (self.faculty.first_name,self.faculty.last_name)

     
     
     
# This is used for Upload Quizes  ==> FACULTY AND ADMIN ACCESS
     
class Quiz(models.Model):
    question=models.TextField()
    option_A=models.TextField()
    option_B=models.TextField()
    option_C=models.TextField(null=True,blank=True)
    option_D=models.TextField(null=True,blank=True)
    right=models.BooleanField(null=True,default=False)
    wrong=models.BooleanField(null=True,default=False)
    quiz_subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    faculty_host=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="+")
    quiz_of_student=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    quize_score=models.DecimalField(max_digits=5,decimal_places=2, null=True,blank=True)
    total_marks=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    def __str__(self) -> str:
        return self.question
   
class Answer(models.Model):
    textAnswer=models.TextField()
    charAnswer=models.CharField(max_length=200)
    question=models.ForeignKey(Quiz,on_delete=models.CASCADE)
# This is used for CLASS ACTIVITIES ==> FACULTY AND ADMIN ACCESS
class ClassActivity(models.Model):
   all_chats=models.ManyToManyField(StudentChat)
   student_name=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)
   topics=models.ManyToManyField(Topic)
   links=models.ManyToManyField(Link)
  
  
  
# This is used for Meet videos thumbnails ==> FACULTY AND ADMIN ACCESS
class VideoThumbnails(models.Model):
    video_img=models.ImageField(upload_to='app/uploads/faculties/class_on_meet/thumb_img',blank=True,null=True)
    name=models.CharField(max_length=150,null=True,blank=True)
    thumbnails=models.ForeignKey('ClassMeet',on_delete= models.CASCADE,null=True)
    
    def __str__(self):
        return f"VideoThumb {self.id}"
    
# This is for uploaded any video ==> FACULTY AND ADMIN ACCESS   
class ClassMeet(models.Model):
    on_subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    live_video=models.FileField(upload_to="app/uploads/faculties/meet/videos",)
    topic_name=models.CharField(max_length=150)
    desc=models.TextField()
    host=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True)
    participants=models.ManyToManyField(MyUser,blank=True,related_name="student_participants")
    created_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f"Video of {self.topic_name} ({self.on_subject}) is uploaded [{self.host}] "


# This is used for ASSIGNMENTS ==> FACULTY AND ADMIN ACCESS
class Assignment(models.Model):
    file=models.FileField(_('assignment_file'),upload_to='app/uploads/students/docs/%y/%m/%d',)
    file_name=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    student_submit=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    desc=models.TextField(null=True,blank=True)
    related_to_sub=models.ForeignKey(Subject,on_delete=models.CASCADE)
    submitted=models.BooleanField(default=False)

    def __str__(self):
        return f"Assignment of {self.related_to_sub} {self.file_name} from {self.student} is submitted"