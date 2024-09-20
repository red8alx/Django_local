from django.contrib import admin
from .models import student
from .models import department
from .models import registeredStudent
from .models import user, profile
from .models import Book, Author

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name')
    search_fields = ('first_name','last_name')
class departmentAdmin(admin.ModelAdmin):
    list_display = ('id','department_name')
    search_fields = ('department_name',)
class registeredStudentAdmin(admin.ModelAdmin):
    list_display = ('id','student_name','department')
    search_fields = ('student_name',)
class userAdmin(admin.ModelAdmin):
    list_display = ('id','username')
    search_fields = ('username',)
class profileAdmin(admin.ModelAdmin):
    list_display = ('id','bio','user')
    search_fields = ('user',)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','author_name')
    search_fields = ('author_name',)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'published_date')
    search_fields = ('title','author')
admin.site.register(student, studentAdmin)
admin.site.register(department, departmentAdmin)
admin.site.register(registeredStudent, registeredStudentAdmin)
admin.site.register(user, userAdmin)
admin.site.register(profile, profileAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)