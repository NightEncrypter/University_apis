from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class SignUp(APIView):
    
    def post(self,request):
        
        return Response('')