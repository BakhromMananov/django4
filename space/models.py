from django.db import models
from django.utils.text import slugify

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=250)
    slug = models.CharField(max_length=250, blank=True, null=True)
    school_info = models.TextField()
    courses = models.ForeignKey('Course', on_delete=models.PROTECT, blank=True, null=True)
    campus = models.ForeignKey('Campus', on_delete=models.PROTECT, blank=True, null=True)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Image', blank=True, null=True)
    feedback = models.ForeignKey('Feedback', on_delete=models.PROTECT, blank=True, null=True)
    contact = models.CharField(max_length=250)
    age=models.ForeignKey('Age', on_delete=models.PROTECT, blank=True, null=True)
    price = models.PositiveBigIntegerField(default=100)
    
    class Meta:
        verbose_name='School'
        verbose_name_plural = 'Schools'
        ordering = ('id',)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    description= models.TextField()
    course_type = models.CharField(max_length=250)
    duration = models.IntegerField(default=1)
    rating = models.ForeignKey('Rating', on_delete=models.PROTECT, blank=True, null=True)
    practice = models.ForeignKey('Practice', on_delete=models.PROTECT, blank=True, null=True)
    price=models.PositiveIntegerField(default=100)
    

    class Meta:
        verbose_name='Course'
        verbose_name_plural = 'Courses'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Campus(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, blank=True, null=True)


    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'
    
    def __str__(self):
        return f'{self.name}'

class Age(models.Model):
    student_age = models.PositiveIntegerField(default=14)

    class Meta:
        verbose_name = 'Age'
        verbose_name_plural = 'Ages'
    
    def __str__(self):
        return f'{self.student_age}'
    
class CourseType(models.Model):
    name=models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name='Course Type'
        verbose_name_plural = 'Course types'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Practice(models.Model):
    name= models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Practice'
        verbose_name_plural = 'Practices'

    def __str__(self):
        return self.name

class Feedback(models.Model):
    comment=models.TextField()

    class Meta:
        verbose_name='Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ('comment',)

    def __str__(self):
        return self.comment
    
class Rating(models.Model):
    rating = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name='Rating'
        verbose_name_plural = 'Ratings'
        ordering = ('rating',)

    def __str__(self):
        return f'{self.rating}'

class SiteUser(models.Model):
    first_name= models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)
    password_repeat = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'