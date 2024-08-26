from django.contrib import admin
from .models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name')
    search_fields = ('first_name','last_name')

admin.site.register(student, studentAdmin)