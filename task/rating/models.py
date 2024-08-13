from django.db import models
from django.contrib.auth.models import User
from users.models import Users

# import rating
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    

class Score(models.Model):
    user = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    rate = models.IntegerField()
    
    
    def __str__(self):
        return f"Rating for {self.article} is {self.rate}"