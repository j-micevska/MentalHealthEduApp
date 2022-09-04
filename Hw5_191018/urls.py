"""Hw5_191018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from MentalHealthEduApp import views
from MentalHealthEduApp.views import register, courses, forum, user_login, profile, helppage, experiences, tests, course_details

urlpatterns = [
    path('', register, name="start"),
    path('admin/', admin.site.urls),
    path('register/', register, name="register"),
    path('login/', user_login, name="user_login"),
    path('courses/', courses, name="courses"),
    path('forum/', forum, name="forum"),
    path('profile/', profile, name="profile"),
    path('experiences/', experiences, name="experiences"),
    path('tests/', tests, name="tests"),
    path('helppage/', helppage, name="helppage"),
    path("courses/<int:id>/", course_details , name="course_details"),
]
