from django.shortcuts import render
# import the logging library

# Create your views here.
def index(request):
    return render(request, 'index.html')
