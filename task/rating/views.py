from django.shortcuts import render
from rating.serializers import ScoreSerializers,Articleserializers
from rating.models import Score,Article
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


# Create your views here.



class ScoreViewSet(ModelViewSet):
    queryset=Score.objects.all()
    serializer_class=ScoreSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class ArticleViewset(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class =Articleserializers
    
    
    
    