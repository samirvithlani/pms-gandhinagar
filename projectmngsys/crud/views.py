from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required
from user.decorators import teacher_required

# Create your views here.
def employee_create_view(request):
    context ={}
    #token
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/crud/list')

    context['form'] = form
    
    return render(request,'crud/employee_create.html',context)
 
@login_required  
@teacher_required
def employee_list_view(request):
    context ={}
    employee = Employee.objects.all().values()
    context['employee'] = employee
    return render(request,'crud/employee_list.html',context)


def employee_delete_view(request,id):
    context ={}
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        deleted = employee.delete()
        print(deleted)
        return HttpResponseRedirect('/crud/list')
    return render(request,'crud/employee_delete.html',context)
    

def employee_detail_view(request,id):
    context ={}
    employee = Employee.objects.get(id=id)
    context['employee'] = employee
    return render(request,'crud/employee_detail.html',context)


def employee_update_view(request,id):
    context = {}
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None,instance=employee)
    if form.is_valid():
        x = form.save()
        return HttpResponseRedirect('/crud/list')
        
    context['form'] = form        
    
    return render (request,'crud/employee_update.html',context)
    