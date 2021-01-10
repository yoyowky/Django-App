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
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)
  
def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})