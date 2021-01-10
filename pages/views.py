from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home_view():
# 	return "<h1>Hello World</h1>"   # string of html code, not django
def home_view(request, *args, **kwargs):
	print(args, kwargs, request);   # () {} <WSGIRequest: GET '/'>
	print(request.user);  # yoyo
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {})     # use html template


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})


def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})