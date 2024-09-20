from django.db import models

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=200)
class employee (models.Model):
    employee_name = models.CharField(max_length=200)
    department = models.ForeignKey(department, on_delete = models.CASCADE, related_name = 'departments')

class product(models.Model):
    product_name = models.CharField(max_length=200)
class productDescription(models.Model):
    description = models.TextField()
    product = models.OneToOneField(product, on_delete = models.CASCADE)

class companyStudent(models.Model):
    student_name = models.CharField(max_length=200)
class companyCourse(models.Model):
    course_name = models.CharField(max_length=200)
    student = models.ManyToManyField(companyStudent, related_name='courses')



