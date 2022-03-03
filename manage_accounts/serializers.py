from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    
    def create(self,validated_data):
      pass
  
    def update(self,validated_data):
        pass

