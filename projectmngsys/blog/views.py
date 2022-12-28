from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Sum,Count,Max,Min,Avg

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
    #students =Student.objects.all().values()
    #students = Student.objects.filter(age__gte=25).values()
    #students = Student.objects.filter(age__lte=25).values()
    #students = Student.objects.filter(name__istartswith='A').values()
    #students = Student.objects.filter(name__endswith='a').values()
    #students = Student.objects.filter(name__contains='a').values()
    #between
    #students = Student.objects.filter(age__range=(20,25)).values()
    #in
    #students = Student.objects.filter(age__in=[20,25]).values()
    #orderby
    #students = Student.objects.all().order_by('-name','-age').values()
    #students = Student.objects.filter(age__gt=24).order_by('-name').values()
    #students =Student.objects.exclude(age__gt=24).order_by('-name').values()
    #students =Student.objects.all().reverse().values()
    #AND
    students = Student.objects.filter(age__gt=24,name__istartswith='A').values()
    #annotate
    #name starts with a count....
    #students = Student.objects.aggregate(total=Max('age')).values()
    students = Student.objects.annotate(total = Min('age')).values()
    print(students)

    #print(students)
    
    return render(request,'blog/getalldata.html',{'students':students})    


def que_ans_vote(request):
    #no of question
    print("count--->",Question.objects.count())
    print("count choice -->",Choice.objects.count())
    #no of choice per question
    #obj = Question.objects.annotate(choice_count =Count('choice')).values()
    #obj = Question.objects.filter(question_text__icontains ="w").annotate(choice_count =Count('choice')).values()
    #obj = Question.objects.annotate(vote_count  =Sum('choice__votes')).values()
    #obj = Question.objects.annotate(vote_count =Sum('choice__votes')).filter(vote_count__isnull=False).order_by('-vote_count')[0]
    #obj = Question.objects.annotate(vote_count = Sum('choice__votes')).filter(vote_count__isnull=True).values()
    #obj = Question.objects.aggregate(vote_count=Min('choice__votes'))
    #find question having highest vote using aggregate
    obj = Question.objects.aggregate(vote_count=Max('choice__votes'))
    
    
    print(obj)
    
    return render(request,'blog/que_ans_vote.html')

def creatOrm(request):
    #objects.all
    #save
    #create an object of student model
    student = Student(age=25,isActive =False)
    student.save()
    print("student saved...")
    return render(request,'blog/createorm.html')


def deleteRecord(request):
    
    #orm -->delete single fetch
    #student = Student.objects.get(name="ram")
    student = Student.objects.filter(name="ram")
    deleted = student.delete()
    print(deleted)
    print("student deleted...")
    
    
    return render(request,'blog/createorm.html')