from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def about(request):
    return HttpResponse("We are at About")
    # return render(request, "shop/index.html")

def search(request):
    return HttpResponse("We are at search")
    # return render(request, "shop/index.html")

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