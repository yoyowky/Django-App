from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home_view():
# 	return "<h1>Hello World</h1>"   # string of html code, not django
def home_view(request, *args, **kwargs):
	print(args, kwargs, request);   # () {} <WSGIRequest: GET '/'>
	print(request.user);  # yoyo
	return HttpResponse("<h1>Hello World</h1>")


def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contact page</h1>")


def about_view(request, *args, **kwargs):
	return HttpResponse("<h1>About page</h1>")


def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social page</h1>")