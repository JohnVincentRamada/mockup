from django.contrib import admin
from .models import UserDetail, Resume, HonorsAwards, Education

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'address', 'contact_number', 'created_at')

admin.site.register(UserDetail, UserDetailAdmin)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',  'linkedin_link', 'summary', 'created_at')

admin.site.register(Resume, ResumeAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'degree', 'year_started', 'year_ended', 'created_at')

admin.site.register(Education, EducationAdmin)

class HonorsAwardsAdmin(admin.ModelAdmin):
    list_display = ('user', 'award', 'organization', 'issued', 'description', 'created_at')

admin.site.register(HonorsAwards, HonorsAwardsAdmin)
