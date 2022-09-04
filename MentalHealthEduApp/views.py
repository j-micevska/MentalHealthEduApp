from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Course, Message
from django.views import generic
from .forms import MessageForm

# Create your views here.


def register(request):
    return render(request,"Register.html")


def login(request):
    return render(request, "Login.html")


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
