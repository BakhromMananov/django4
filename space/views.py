from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Min, Max



from .models import *
from .forms import *


def index(request):
    schools = School.objects.all()
    campus = Campus.objects.all()
    min_price =School.objects.aggregate(Min('price'))['price__min']
    max_price=School.objects.aggregate(Max('price'))['price__max']
    mes = None


    min_filter = request.GET.get('min_price', min_price)
    max_filter = request.GET.get('max_price', max_price)
    
    school_post = request.GET.get('school_name')
    
    campus_post = request.GET.get('campus')

    
    if school_post:
        schools = schools.filter(name__icontains = 
        school_post)
    
    if campus_post:
        schools = schools.filter(name__icontains = campus_post)

    if min_filter and max_filter:
        schools = schools.filter(
            price__gte=min_filter,
            price__lte=max_filter
        )

    paginator = Paginator(schools, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'space/index.html', {'schools': schools, 'campus': campus, 'page_obj': page_obj, 'mes': mes, 'min_price': min_price, 'max_price': max_price })

def school(request, school_slug):
    school = get_object_or_404(School, slug = school_slug)

    return render(request, 'space/school.html', {'school': school})

def course(request, course_slug):
    course = get_object_or_404(Course, slug = course_slug)

    return render(request, 'space/course.html', {'course': course})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = LoginForm()
    mes = None

    if request.method == 'POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                mes= messages.success(request, f'{username} you entered your working space!')
                return redirect('home')
        else:
            mes = messages.error(request, f'{username} or password are wrong')
            
    return render(request, 'space/login.html', {'form': form, 'mes': mes })

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home')

def user_register(request):
    mes = None
    user = None

    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)

            messages.success(request, f'{user} you created your profile')
            return redirect('home')
        
        else:
            messages.error(request, f'{user} you entered something wrong')
    return render(request, 'space/register.html', {'form': form})


def user_profile(request):
    mes = None

    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST)
    

        if form.is_valid():
            form.save()
            mes = messages.success(request, f'{request.user.username} your profile has been updated')
            return redirect('home')
    
    return render(request, 'space/user.html', {'form': form, 'mes': mes})
