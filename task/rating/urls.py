from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ScoreViewSet,ArticleViewset

router = DefaultRouter()
router.register('score', ScoreViewSet)
router.register('article', ArticleViewset)


urlpatterns = [
]

urlpatterns += router.urls