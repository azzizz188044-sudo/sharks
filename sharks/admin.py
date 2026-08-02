from django.contrib import admin
from .models import Teacher, Result

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id',)
