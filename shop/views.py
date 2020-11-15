from django.shortcuts import render, HttpResponse
from shop.models import  Product
# Create your views here.


def index(request):
    # return HttpResponse("Index page")

    products = Product.objects.all()
    print (products)
    data = {
        'products': products
    }
    return render(request, 'index.html', data)

def login(request):
    #return HttpResponse("Login page")
    return render(request, 'login.html')


def productDetails(request , product_id):
    product = Product.objects.get(id = product_id)
    #return HttpResponse(product.id)
    return render(request, 'product_details.html', {'product': product})
