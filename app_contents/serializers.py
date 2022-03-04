from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class DocxSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
        
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class StudentChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class FacultyChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
        
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__" 
        
        
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields="__all__" 