from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.
from rest_framework import status
from app_contents.models import Student,Faculty,SubjectVideo,SubjectDocx,SubjectImage,Link,Topic,Unit,Subject,StudentChat,FacultyChat,Quiz,ClassActivity,Assignment,ClassMeet,VideoThumbnails
from .serializers import TopicSerializer, VideoSerializer,ImageSerializer,LinkSerializer,FacultySerializer,DocxSerializer,UnitSerializer,SubjectSerializer

# UPLOADING A VIDEO
class SubjectVideoView(APIView):
    serializer_class=VideoSerializer
    def get(self,request):
        
       
            data_query=SubjectVideo.objects.all()
            serializer=VideoSerializer(data_query,many=True)
            
            response=serializer.data
            return Response({"videos":response})
       

    
    def post(self,request):
        serializer=VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your video {video_name}, ID no {video_id} is saved".format(video_name=serializer.data["video_name"],video_id=serializer.data["id"]),
                             })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#VIDEO ==> UPDATE DELETE GET 
class Video_Update_Delete(APIView):
    serializer_class=VideoSerializer
    
    def get_obj(self,data):
        try:
            
            return get_object_or_404(SubjectVideo,id=data)
        except SubjectVideo.DoesNotExist:
            raise Http404
            
    def get(self,request,pk,format=None):
        snippet=self.get_obj(pk)
        serializer=VideoSerializer(snippet)
        
        response=serializer.data
        return Response({"videos":response})
    
    def put(self,request,pk,format=None):
        try:
            snippet=self.get_obj(pk)
            
            serializer=VideoSerializer(snippet ,data=request.data)
            if serializer.is_valid():
                upd_obj=serializer.save()
                return Response({"msg":"your video {video_name}, ID no {video_id} is updated".format(video_name=serializer.data["video_name"],video_id=upd_obj.id),
                             })
        except SubjectVideo.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,pk,format=None):
        try:
            snippet=self.get_obj(pk)
            serializer=VideoSerializer(snippet)
            obj_id,obj_name=snippet.id,snippet.video_name
            # print(snippet.id,"inst")
           
            snippet.delete()
            # print(delete_inst,"del inst")
            
            return Response({"msg":"your {name} of {id} is deleted".format(id=obj_id,name=obj_name),
                           })
        except SubjectVideo.DoesNotExist:
             return Response("Data not found", status=status.HTTP_400_BAD_REQUEST)


# ----------------
   
# UPLOADING A IMAGE
class SubjectImageView(APIView):
    serializer_class=ImageSerializer
    def get(self,request):
        try:
            
            data_query=SubjectImage.objects.all()
            # print(data_query)
            serializer=ImageSerializer(data_query,many=True)
            
            response=serializer.data
            # print(response,"get_img")
            return Response(response)
        except SubjectImage.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        
            serializer=ImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                print(serializer.data)
                # return Response({"msg":"your image {img_name} of Id {id} is saved".format(img_name=serializer.data["image_name"],id=serializer.data['id'])})
                return Response(serializer.data)
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# IMAGE ==> UPDATE DELETE GET 
class Image_Update_Delete(APIView):
    serializer_class=ImageSerializer
    
    # HELPER FUNCTION
    def get_obj(self,data):
      
            return get_object_or_404(SubjectImage,id=data)
       
         
    def get(self,request,pk):
            try:
                snippet=self.get_obj(pk)
            
                if snippet:
                    serializer=ImageSerializer(snippet)
                    return Response({"images":serializer.data})
                
            except SubjectImage.DoesNotExist :
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            
    def put(self,request,pk):
        try:
            snippet=self.get_obj(pk)
            if snippet:
                serializer=ImageSerializer(snippet,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"images":"your video {img_name}, ID no {id} is updated".format(img_name=serializer.data["image_name"],id=serializer.data['id'])})
        except SubjectImage.DoesNotExist :
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            
    def delete(self,request,pk):
        
        try:
            snippet=self.get_obj(pk)
            
            if snippet:
                obj=snippet.delete()
                print(obj)
                return Response({"msg":"your image {id} is deleted".format(id=obj)})
        except SubjectImage.DoesNotExist :
            return Response("Image does not exist",status=status.HTTP_404_NOT_FOUND)
        
# ----------------
    
# UPLOADING A LINK
class LinkView(APIView):
    
    serializer_class=LinkSerializer
    
    

    
    def get(self,request):
        
        try:
            data_query=Link.objects.all()
            serializer=LinkSerializer(data_query,many=True)
            
            response=serializer.data
            return Response(response)
        except Link.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def post(self,request):
        
            # print(request.data)
             
            serializer=LinkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"your link {link_name} is saved".format(link_name=serializer.data["link_name"])})
         
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
   
#LINK ==> UPDATE DELETE GET 
class Link_Update_Delete(APIView):
    serializer_class=LinkSerializer
    
    # HELPER FUNC
    def get_obj(self,data):
            try:
                linkquery=get_object_or_404(Link,id=data)
                return linkquery
            except Link.DoesNotExist:
                raise Http404
    
    # SINGLE OBJ
    def get(self,request,pk):
        try:
            snippet=self.get_obj(pk)
            if snippet:
                serializer=LinkSerializer(snippet)
            return Response(serializer.data)    
        
        except:
            return Response("Link not found",status=status.HTTP_404_NOT_FOUND)
        
        
    # Update 
    def put(self,request,pk):
        # try:
        snippet=self.get_obj(pk)
        print(snippet,"exist")
        if snippet:
                serializer=LinkSerializer(snippet,    data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response({"msg":'your {link_id} is updated'.format(link_id=serializer.data['id']),"data":serializer.data})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        

    def delete(self,request,pk):
        snippet=get_object_or_404(Link,id=pk)
        if snippet:
            snippet.delete()
            return Response({"msg":"Link is deleted"},status=status.HTTP_202_ACCEPTED)
        return Response("Link not found")


# ----------------------

# UPLOADING A DOCX
class DocxView(APIView):
    
    parser_classes=[FormParser,MultiPartParser]
    serializer_class=DocxSerializer
    def get(self,request):
        try:
            data_query=SubjectDocx.objects.all()
            serializer=DocxSerializer(data_query,many=True)
            
            response=serializer.data
            return Response({"docx":response})
    
        except SubjectDocx.DoesNotExist:
            return Response("Not found",status=status.HTTP_404_NOT_FOUND)
            
    def post(self,request,format=None):
        print(request.data)
        
        serializer=DocxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your doc {file_name} is saved".format(file_name=serializer.data["file_name"]) })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  
#DOCX ==> UPDATE DELETE GET 
class Docx_Update_Delete(APIView):
    serializer_class=DocxSerializer
    
    # HELPER FUNC
    def get_obj(self,data):
            try:
                linkquery=get_object_or_404(SubjectDocx,id=data)
                return linkquery
            except SubjectDocx.DoesNotExist:
                raise Http404
    
    # SINGLE OBJ
    def get(self,request,pk):
        try:
            snippet=self.get_obj(pk)
            if snippet:
                serializer=DocxSerializer(snippet)
            return Response(serializer.data)    
        
        except:
            return Response("Docx not found",status=status.HTTP_404_NOT_FOUND)
        
        
    # Update 
    def put(self,request,pk):
        snippet=self.get_obj(pk)
        print(snippet,"exist")
        if snippet:
                serializer=DocxSerializer(snippet,    data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response({"msg":'your {docx_name} of ID {docx_id} is updated'.format(docx_name=serializer.data['file_name'],docx_id=serializer.data['id']),"data":serializer.data})
        
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Link not found",status=status.HTTP_404_NOT_FOUND)       
        

    def delete(self,request,pk):
        snippet=get_object_or_404(Link,id=pk)
        if snippet:
            snippet.delete()
            return Response({"msg":"Link is deleted"},status=status.HTTP_202_ACCEPTED)
        return Response("Link not found", status=status.HTTP_400_BAD_REQUEST)


# ----------------------

#  UPLOADING A TOPIC
class TopicView(APIView):
    serializer_class=TopicSerializer
    
    def get(self,request):
        try:
            snippet=Topic.objects.all()
            serializer=TopicSerializer(snippet,many=True)
        
            return Response( serializer.data) 
        except:
            return Response("Topic not found",status=status.HTTP_404_NOT_FOUND) 
    def post(self,request):
            serializer=TopicSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data) 
        
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
 #TOPIC ==> UPDATE DELETE GET        
class Topic_Update_Delete(APIView):
    serializer_class=TopicSerializer
    
    def get_obj(self,data):
        try:
            return get_object_or_404(Topic,id=data)
        except Topic.DoesNotExist :
            raise Http404
    def get(self,request,pk):
        
        snippet=self.get_obj(pk)
        if snippet:
            serializer=TopicSerializer(snippet,many=True)
            return Response(serializer.data)
        return Response("Topic not found",status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk):
        
        snippet=self.get_obj(pk)
        if snippet:
            serializer=TopicSerializer(snippet,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                return Response({"msg":"Your topic {name} of Id {id}  is updated".format(name=serializer.data['topic_name'],id=serializer.data['id'])})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Topic not found",status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        snippet=self.get_obj(pk)
        if snippet:
            snippet.delete()
            return Response({"msg":"Your topic is deleted"})
        
        return Response("Topic not found",status=status.HTTP_404_NOT_FOUND)
   
 
 
# -------------------------



#  UPLOADING A UNIT
class UnitView(APIView):
    serializer_class=UnitSerializer
    
    def get(self,request):
        try:
            snippet=Unit.objects.all()
            serializer=UnitSerializer(snippet,many=True)
        
            return Response( serializer.data) 
        except:
            return Response("Unit not found",status=status.HTTP_404_NOT_FOUND) 
    def post(self,request):
            serializer=UnitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data) 
        
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
                   
               
 #UNIT ==> UPDATE DELETE GET        
class Unit_Update_Delete(APIView):
    serializer_class=UnitSerializer
    
    def get_obj(self,data):
        try:
            return get_object_or_404(Unit,id=data)
        except Unit.DoesNotExist :
            raise Http404
    def get(self,request,pk):
        
        snippet=self.get_obj(pk)
        if snippet:
            serializer=UnitSerializer(snippet,many=True)
            return Response(serializer.data)
        return Response("Unit not found",status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk):
        
        snippet=self.get_obj(pk)
        if snippet:
            serializer=UnitSerializer(snippet,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                return Response({"msg":"Your unit {name} of Id {id}  is updated".format(name=serializer.data['name'],id=serializer.data['id'])})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Unit not found",status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        snippet=self.get_obj(pk)
        if snippet:
            snippet.delete()
            return Response({"msg":"Your Unit is deleted"})
        
        return Response("Unit not found",status=status.HTTP_404_NOT_FOUND)
          



#  UPLOADING A Subject
class SubjectView(APIView):
    serializer_class=SubjectSerializer
    
    def get(self,request):
        try:
            snippet=Subject.objects.all()
            serializer=SubjectSerializer(snippet,many=True)
        
            return Response( serializer.data) 
        except:
            return Response("Subject not found",status=status.HTTP_404_NOT_FOUND) 
        
    def post(self,request):
            serializer=SubjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data) 
        
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


#  SUBJECT ==> UPDATE DELETE GET        
class Subject_Update_Delete(APIView):
    

    
    
    serializer_class=SubjectSerializer
    
    def get_obj(self,data):
        try:
            return get_object_or_404(Subject,id=data)
        except Subject.DoesNotExist :
            raise Http404
    def get(self,request,pk):
        
        snippet=self.get_obj(pk)
        if snippet:
            serializer=SubjectSerializer(snippet)
            return Response(serializer.data)
        return Response("Subject not found",status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk):
        
        snippet=self.get_obj(pk)
        if snippet:
            serializer=SubjectSerializer(snippet,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                return Response({"msg":"Your Subject {name} of Id {id}  is updated".format(name=serializer.data['name'],id=serializer.data['id'])})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Subject not found",status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        snippet=self.get_obj(pk)
        if snippet:
            snippet.delete()
            return Response({"msg":"Your Subject is deleted"})
        
        return Response("Subject not found",status=status.HTTP_404_NOT_FOUND)
    
    
    
    
    
    
class FilterOfUnit(APIView):
        
        def query_set(self):
            return Subject.objects.filter(name__icontains='VLSI')
            
        def get(self,request):
            
            # un=self.query_set()
            
            # data_query=un.unit.all()
            # print(data_query)
            # all_categories = Category.objects.filter(
            # id__in=Blogpost.categories.through.objects.filter(
            #     blogpost__in=qs
            # ).values('category_id')
            
            
            # sub=Unit.objects.create()
            # un=sub.all()
            
            # print(sub)
            # print(un)
            return Response("done")
        