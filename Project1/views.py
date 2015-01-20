

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, "home.html", {})

def bio(request):
	return render(request, "bio.html", {})

def disc(request):
	return render(request, "disc.html", {})

def tour(request):
	return render(request, "tour.html", {})