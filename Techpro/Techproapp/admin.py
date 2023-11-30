from django.contrib import admin
from .models import User, UserCourse, Course, Admission, InternApply, Contributor, Collaborator, Task

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'verification_code', 'is_verified', 'full_name', 'location', 'state_passcode', 
                    'username', 'digital_skills', 'twitter_handle', 'facebook_handle', 'linkedin_handle' )


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration')


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_applied', 'status')


@admin.register(InternApply)
class InternApplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'location_choices', 'location')


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'upload_image', 'progress')                       