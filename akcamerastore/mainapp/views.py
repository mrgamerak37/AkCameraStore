from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Camera

# Create your views here.

# view for index page
def index(request):

    product = Camera.objects.all()
    f_product = []
    for i in product:
        if i.carousel:
            f_product.append(i)

    return render(request, 'index.html', {'product':f_product})

def product(request, id):
    last = Camera.objects.all().filter(id=id)
    
    return render((request), 'product.html', {'product':last})

def store(request):
    if(request.method == 'POST'):
        p_name = request.POST.get('search-item')
        price = request.POST.getlist('price')
        brand = request.POST.getlist('brand')
        product = None

        # conditions for price 
        # if price:
        #     print(price)
        #     if 'price1' in price:
        #         product = Camera.objects.all().filter(price__range = (0, 10000))
        #     elif 'price2' in price:
        #         product = Camera.objects.all().filter(price__range = (10000, 20000))
        #     elif 'price3' in price:
        #         product = Camera.objects.all().filter(price__range = (20000, 2000000))
        #     return render(request, 'store.html', {'product':product})
        
        if p_name:
            product = Camera.objects.all().filter(name__contains = p_name)
            return render(request, 'store.html', {'product':product})
    
    product = Camera.objects.all()

    return render(request, 'store.html', {'product':product})