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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from MentalHealthEduApp.views import register, courses, forum, user_login, profile, helppage
from MentalHealthEduApp.views import experiences, tests, course_details, delete_message, user_logout

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
    path("courses/<int:id>/", course_details, name="course_details"),
    path("delete/<message_id>/", delete_message, name='delete_message'),
    path('logout/', user_logout, name='user_logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)