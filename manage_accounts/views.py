from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class SignUp(APIView):
    
    def post(self,request):
        
        return Response('')
    
    
class Home(APIView):
    
    
    def get(self,request):
        
        return Response(["Hello","how are you"])