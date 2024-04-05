from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializer import Studserializer
from .models import *
from rest_framework import status


class Studapi(APIView):
    def get(self, request,id=None, format=None):
        if id is not None:
            qs=Studs.objects.get(id=id)
            sd=Studserializer(qs)
            return Response(sd.data)
        stu=Studs.objects.all()
        sd=Studserializer(stu,many=True)
        return Response(sd.data)
    
    def post(self, request,id=None, format=None):
        data=request.data
        sd=Studserializer(data=data)
        if sd.is_valid():
            sd.save()
            return Response({"msg":"Data saved successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(sd.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id=None,format=None):
        stud=Studs.objects.get(id=id)
        sd=Studserializer(stud,data=request.data)
        if sd.is_valid():
            sd.save()
            return Response({"msg":"Data updated successfully"},status=status.HTTP_200_OK) 
        return Response(sd.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id=None,format=None):
        stud=Studs.objects.get(id=id)
        sd=Studserializer(stud,data=request.data,partial=True)
        if sd.is_valid():
            sd.save()
            return Response({"msg":"Data updated successfully"},status=status.HTTP_200_OK) 
        return Response(sd.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id=None,format=None):
        stud=Studs.objects.get(id=id)
        stud.delete()
        return Response({"msg":"Data deleted successfully"},status=status.HTTP_200_OK)
        




# @api_view(['GET', 'POST','DELETE','PUT','PATCH'])
# def Studapi(request,id=None):
#     if request.method =='GET':
#         # id=request.data.get(id)
#         if id is not None:
#             qs=Studs.objects.get(id=id)
#             sd=Studserializer(qs)
#             return Response(sd.data)
#         stu=Studs.objects.all()
#         sd=Studserializer(stu,many=True)
#         return Response(sd.data)
    
#     if request.method == 'POST':
#         data=request.data
#         sd=Studserializer(data=data)
#         if sd.is_valid():
#             sd.save()
#             return Response({"msg":"Data saved successfully"})
#         else:
#             return Response(sd.errors)
        
#     if request.method == 'PUT':
#         stud=Studs.objects.get(id=id)
#         sd=Studserializer(stud,data=request.data)
#         if sd.is_valid():
#             sd.save()
#             return Response({"msg":"Data updated successfully"}) 
#         return Response(sd.errors)      
     
#     if request.method == 'PATCH':
#         stud=Studs.objects.get(id=id)
#         sd=Studserializer(stud,data=request.data,partial=True)
#         if sd.is_valid():
#             sd.save()
#             return Response({"msg":"Data updated successfully"}) 
#         return Response(sd.errors) 

#     if request.method == 'DELETE':
#         stud=Studs.objects.get(id=id)
#         stud.delete()
#         return Response({"msg":"Data deleted successfully"})



