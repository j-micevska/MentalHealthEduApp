from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Course, Message
from .forms import MessageForm, RegisterForm
from django.contrib.auth import authenticate, login
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
            return render(request, 'Courses.html')
        else:
            return render(request, 'Login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'Login.html')


def courses(request):
    context = {"courses": Course.objects.all()}
    return render(request, "Courses.html", context=context)


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


def search(request):
    model = Course
    template_name = 'Search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Course.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


def helppage(request):
    return render(request, "HelpPage.html")


def tests(request):
    return render(request, "Tests.html")


def profile(request):
    return render(request, "Profile.html")


def experiences(request):
    return render(request, "Experiences.html")
