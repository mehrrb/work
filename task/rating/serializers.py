from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rating.models import Score,Article


class ScoreSerializers(ModelSerializer):
    
    
    class Meta:
        model = Score
        fields = '__all__'
        
    def validate_rate(self,value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('Rate must be between 0 and 5')
        return value
    
    
    
class Articleserializers(ModelSerializer):
    
    
    class Meta:
        model = Article
        fields = '__all__'