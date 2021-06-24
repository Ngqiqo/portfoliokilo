from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "about.html")

def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "contact.html")

def skills(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "skills.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
