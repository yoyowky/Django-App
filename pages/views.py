from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home_view():
# 	return "<h1>Hello World</h1>"   # string of html code, not django
def home_view(*args, **kwargs):
	return HttpResponse("<h1>Hello World</h1>")