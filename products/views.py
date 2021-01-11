from django.shortcuts import render
from .forms import ProductForm
from .models import Product 

# Create your views here.

# use django form
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     obj = Product.objects.get(id=1)
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)


def product_create_view(request):
    # print('get11111', request.GET)
    # print('post11111', request.POST)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print('my_new_title', my_new_title)
        # Product.objects.create(title=my_new_title)
    context = {}
    return render(request, "product/product_create.html", context)




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