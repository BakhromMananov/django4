from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='home'), 
    path('school/<slug:school_slug>/', school, name='school'),
    path('course/<slug:course_slug>/', course, name='course'), 
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'), 
    path('register/', user_register, name='register'), 
    path('profile/', user_profile, name='profile')
]
