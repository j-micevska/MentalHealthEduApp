from django.contrib import admin
from .models import Message, Course

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    model = Message
    search_fields = ["title", "content"]


admin.site.register(Message, MessageAdmin)


class CourseAdmin(admin.ModelAdmin):
    model = Course
    search_fields = ["name", "symptoms", "help"]


admin.site.register(Course, CourseAdmin)
