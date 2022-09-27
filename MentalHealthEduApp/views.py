from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Course, Message
from .forms import MessageForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.


def register(request):
    template = 'Register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return redirect("courses")

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
        context = {"form": RegisterForm}
    return render(request, "Register.html", context=context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("courses")
        else:
            return render(request, 'Login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'Login.html')


def user_logout(request):
    if request.user.is_authenticated == True:
        logout(request)
        return redirect("register")


@login_required()
def courses(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        context = {"courses": Course.objects.filter(name__icontains=str(keyword))}
        return render(request, "Courses.html", context=context)
    else:
        context = {"courses": Course.objects.all()}
        return render(request, "Courses.html", context=context)


@login_required()
def course_details(request, id):
    context = {"course": Course.objects.get(id=id)}
    return render(request, "Course.html", context=context)


@login_required()
def forum(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.author = request.user
            message.save()
            return redirect("forum")
    context = {"messages": Message.objects.all(), "form": MessageForm}
    return render(request, "Forum.html", context=context)


@login_required()
def helppage(request):
    return render(request, "HelpPage.html")


@login_required()
def tests(request):
    return render(request, "Tests.html")


@login_required()
def profile(request):
    context = {"messages": Message.objects.filter(author=request.user)}
    return render(request, "Profile.html", context=context)


@login_required
def delete_message(request,message_id=None):
    if request.user.is_authenticated == True:
        message_to_delete = Message.objects.get(id=message_id)
        message_to_delete.delete()
        return redirect("profile")


@login_required()
def experiences(request):
    return render(request, "Experiences.html")
