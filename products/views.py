from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import ProductForm, RawProductForm
from .models import Product 

# Create your views here.

# use django model form to save data
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    obj = Product.objects.get(id=1)
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

# use raw html form to save data
# def product_create_view(request):
#     # print('get11111', request.GET)
#     # print('post11111', request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print('my_new_title', my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "product/product_create.html", context)

# use django form to save data ,has validation
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print('cleaned_data11111', my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print('form_errors1111', my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "product/product_create.html", context)



def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    #     'featured': obj.featured
    # }
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "My title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)  # instance is the initial data(obj from db) 
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

def dynamic_look_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "product/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # POST request
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all();
    context = {
        "object_list": queryset
    }
    return render(request, "product/product_list.html", context)