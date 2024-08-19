from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class SchoolAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'campus', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    # list_select_related = ('campus', 'courses')
    
    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photos.url}" width="100" height="50"/>')

admin.site.register(School, SchoolAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'course_type')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)

class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ("name",)}

admin.site.register(Campus, CampusAdmin)

class AgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_age')
    list_display_links = ('id', 'student_age')
    search_fields = ('student_age',)
    list_filter = ('student_age',)

admin.site.register(Age, AgeAdmin)

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(CourseType, CourseTypeAdmin)


class PracticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Practice, PracticeAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', 'comment')
    search_fields = ('comment',)
    list_filter = ('comment',)



admin.site.register(Feedback, FeedbackAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating')
    list_display_links = ('id', 'rating')
    search_fields = ('rating',)
    list_filter = ('rating',)

admin.site.register(Rating, RatingAdmin)


class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email')
    list_display_links = ('id', 'first_name', 'last_name', 'username')
    search_fields = ('first_name',)
    list_filter = ('first_name',)

admin.site.register(SiteUser, SiteUserAdmin)