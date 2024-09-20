from django.db import models

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=200)

class registeredStudent(models.Model):
    student_name = models.CharField(max_length=200)
    department = models.ForeignKey(department, on_delete=models.CASCADE, related_name='departments')

class user(models.Model):
    username = models.CharField(max_length=100)

class profile(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(user, on_delete=models.CASCADE)
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'authors')
    published_date = models.DateField()

class student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
