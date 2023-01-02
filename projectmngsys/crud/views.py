from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeForm
from .models import Employee

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
            
def employee_list_view(request):
    context ={}
    employee = Employee.objects.all().values()
    context['employee'] = employee
    return render(request,'crud/employee_list.html',context)