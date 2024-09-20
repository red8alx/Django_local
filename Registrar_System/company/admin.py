from django.contrib import admin
from .models import department, employee
from .models import product, productDescription
from .models import companyStudent, companyCourse


# Register your models here.
class departmentAdmin(admin.ModelAdmin):
    list_display = ('id','department_name')
    search_fields = ('department_name',)
class employeeAdmin(admin.ModelAdmin):
    list_display = ('id','employee_name', 'department')
    search_fields = ('employee_name',)
class productAdmin(admin.ModelAdmin):
    list_display = ('id','product_name')
    search_fields = ('product_name',)
class productDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'product')
    search_fields = ('description',)
class companyStudentAdmin(admin.ModelAdmin):
    list_display = ('id','student_name')
    search_fields = ('student_name',)
class companyCourseAdmin(admin.ModelAdmin):
    list_display = ('id','course_name')
    search_fields = ('course_name',)


admin.site.register(department, departmentAdmin)
admin.site.register(employee, employeeAdmin)
admin.site.register(product, productAdmin)
admin.site.register(productDescription, productDescriptionAdmin)
admin.site.register(companyStudent, companyStudentAdmin)
admin.site.register(companyCourse, companyCourseAdmin)

