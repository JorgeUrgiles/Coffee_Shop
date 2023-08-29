from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def service(request):
    return render(request, "core/service.html")


def menu(request):
    return render(request, "core/menu.html")

def testimonial(request):
    return render(request, "core/testimonial.html")


def reservation(request):
    return render(request, "core/reservation.html")


def contact(request):
    return render(request, "core/contact.html")
