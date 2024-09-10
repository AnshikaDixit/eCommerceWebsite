from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    print("catProds ==>")
    print({catprods})
    cats= {item["category"] for item in catprods}
    print("cats ==>")
    print(cats)
    for cat in cats:
        print("cat ==>")
        print(cat)
        prod=Product.objects.filter(category=cat)
        print("prod ==>")
        print(prod)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        print("nslides ==>")
        print(nSlides)
        allProds.append([prod, range(1, nSlides), nSlides])
        print("allProds ==>")
        print(allProds)


    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    # return HttpResponse("We are at About")
   return render(request, "shop/about.html")

def search(request):
    # return HttpResponse("We are at search")
    return render(request, "shop/about.html")

def contact(request):
    # return render(request, "shop/index.html")
     return HttpResponse("We are at Contact")

def tracker(request):
    # return render(request, "shop/index.html")
     return HttpResponse("We are at Tracker")

def prodView(request):
    # return render(request, "shop/index.html")
     return HttpResponse("We are at Prod View")

def checkout(request):
    # return render(request, "shop/index.html")
      return HttpResponse("We are at Checkout")