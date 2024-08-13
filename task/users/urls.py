from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf.urls import include
from users import views

router = SimpleRouter()
router.register("users_manager",viewset=views.UsersView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
urlpatterns+=router.urls
