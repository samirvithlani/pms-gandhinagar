from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")
    
def aboutus(request):
    context ={}
    name = "Django"
    price = 100
    context['name'] = name
    context['price'] = price
    return render(request,'aboutus.html',context)    

def contactus(request):
    
    return render(request,'blog/contactus.html',{
        'name':'Django',
        'email':'django@gmail.com'
    })