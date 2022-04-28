from dataclasses import fields
from django.contrib import admin

from .models import Student, Track

# Register your models here.


class Customstudent(admin.ModelAdmin):
    fieldsets = (

        ['Student Information', {'fields': [
            'first_name', 'last_name', 'age']}],

        ['Scholarship info', {'fields': ['student_track']}]
    )

    list_display = ('id', 'first_name', 'last_name',
                    'age', 'student_track', 'is_adult')

    search_fields = ('first_name', 'last_name', 'age',
                     'student_track__track_name')

    list_filter = ('age', 'student_track__track_name')


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 1


class Customtrack(admin.ModelAdmin):
    inlines = [InlineStudent]


admin.site.register(Student, Customstudent)
admin.site.register(Track, Customtrack)
