from django.forms import CharField
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from app_contents.models import Student,Faculty,SubjectVideo,SubjectDocx,SubjectImage,Link,Topic,Unit,Subject,StudentChat,FacultyChat,Quiz,ClassActivity,Assignment,ClassMeet,VideoThumbnails
from rest_framework.validators import UniqueValidator




class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectVideo
        fields="__all__" 
    # def validate_video_name(self,value):
    #     isexist=SubjectImage.objects.get(video_name__icontains=value)
        
    #     if isexist:
    #         raise serializers.ValidationError(
    #             "This image is Already added in a list"
    #         )
    #     return value
        

        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields="__all__" 
        depth=1

    # def validate_link_name(self,value):
    #         # print("runner")
    #         isexist=get_object_or_404(Link,link_name__icontains=value)
            
    #         if isexist:
    #             raise serializers.ValidationError("This link is Already added in a link"
    #             )
    #         return value 
     # link_name=serializers.CharField(
        #     max_length=200,
        #     validators=[UniqueValidator(
        #         queryset=Link.objects.all(),
        #     )]
        # )
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectImage
        fields="__all__" 
        
    # # Image ADD
    # def validate_image_name(self,value):
    #     isexist=get_object_or_404(SubjectImage,image_name__icontains=value,)
        
    #     if isexist:
    #         raise serializers.ValidationError(
    #             "This image is Already added in a list"
    #         )
    #     print("aaded")
    #     return value
        
  
        
    
class DocxSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectDocx
        fields="__all__" 
    def validate_link_name(self,val):
        isexist=Link.objects.get("link")
        
        
class TopicSerializer(serializers.ModelSerializer):
    # links = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(),many=False, read_only=True)
    files = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # depth=1
        model=Topic
        fields="__all__" 
        
        
class SubjectSerializer(serializers.ModelSerializer):
    # units = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # depth=1
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
    # topics = serializers.HyperlinkedRelatedField( read_only=True,
    #     view_name='topic-detail',many=True)
    class Meta:
        # depth=1
        model=Unit
        fields="__all__" 
        
        
# class SubjectSerializer(serializers.ModelSerializer):
#     model=Subject
#     class Meta:
#         fields="__all__" 


