from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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

def getAllData(request):
    
    #select name from student
    #django orm lookups
    #students =Student.objects.all().val  ues()
    #students = Student.objects.filter(age__gte=25).values()
    #students = Student.objects.filter(age__lte=25).values()
    students = Student.objects.filter(name__startswith='a').values()
    
    
    
    print(students)
    
    return render(request,'blog/getalldata.html',{'students':students})    