from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Resume, Education, HonorsAwards, UserDetail
from  django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
        
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('user', 'profile_picture', 'address', 'contact_number', 'created_at')

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('linkedin_link', 'summary', 'created_at')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('school', 'image', 'degree', 'year_started', 'year_ended', 'created_at')

class HonorsAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HonorsAwards
        fields = ('image', 'award', 'organization', 'issued', 'description', 'created_at')


