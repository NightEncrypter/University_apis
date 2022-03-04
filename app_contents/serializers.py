from rest_framework import serializers
from app_contents.models import Student,Faculty,SubjectVideo,SubjectDocx,SubjectImage,Link,Topic,Unit,Subject,StudentChat,FacultyChat,Quiz,ClassActivity,Assignment,ClassMeet,VideoThumbnails
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectVideo
        fields="__all__" 
        
        
        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields="__all__" 
        
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectImage
        fields="__all__" 
class DocxSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectDocx
        fields="__all__" 
        
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields="__all__" 
        
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields="__all__" 
        
        
class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ClassActivity
        fields="__all__" 
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__" 
        
class StudentChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=StudentChat
        fields="__all__" 
        
class FacultyChatSerializer(serializers.ModelSerializer):
    model=FacultyChat
    class Meta:
        fields="__all__" 
        
class FacultySerializer(serializers.ModelSerializer):
    model=Faculty
    
    class Meta:
        fields="__all__" 
        
class UnitSerializer(serializers.ModelSerializer):
    model=Unit
    class Meta:
        fields="__all__" 
        
        
# class SubjectSerializer(serializers.ModelSerializer):
#     model=Subject
#     class Meta:
#         fields="__all__" 