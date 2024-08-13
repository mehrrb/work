from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from .models import Users
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
     
    







































# class UsersView(ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer
    
    
#     def post(self,request):
#         data = request.data
#         ser_data = UserSerializer(request,data=data)
#         if ser_data.is_valid():
#             ser_data.context.update({"request":request})
#             ser_data.create(ser_data.validated_data)
#             try:
#                 user = Users.objects.get(email=ser_data.validated_data['email'])
#                 token = str(RefreshToken.for_user(user).access_token)
#                 return Response({"info":"user created"},status=status.HTTP_201_CREATED)
#             except:
#                 logging.error(traceback.format_exc())
#                 return Response({"error":"somthing wrong happen"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
        