from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('user/', views.UserSet.as_view(), name='user'),
    path('resume/', views.ResumeSet.as_view(), name='resume'),
    path('userdetail/', views.UserDetailSet.as_view(), name='user_detail'),
    path('education/', views.EducationSet.as_view(), name='education'),
    path('honorawards/', views.HonorsAwardsSet.as_view(), name='honorawards'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]