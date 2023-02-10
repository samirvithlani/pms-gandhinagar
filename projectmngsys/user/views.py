from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import TeacherSignUpForm,StudentSignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Eletronics,Document
from .forms import ElectronicsForm,DocumentForm
from django.views.generic import ListView

# Create your views here.
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'user/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'user/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        #get email from form valid...
        email = form.cleaned_data.get('email')
        print(email)
        
        res = sendMail(email)
        if res>0:
            user = form.save()
            login(self.request, user)
        return redirect('/')    
    
class LoginView(LoginView):
    
    template_name = 'user/login.html'
    
    def get(self, request, *args, **kwargs):
        print(self.request.user)
        # if self.request.user.is_teacherrr:
        #     print('teacher')
        # else:
        #     print('student')    
        return self.render_to_response(self.get_context_data())

#user email -->
def sendMail(mailid):
    subject = 'Welcome to Project Management System'
    message = 'Thank you for registering with us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mailid]
    res = send_mail(subject, message, email_from, recipient_list)
    print(res)
    return res
    

def upload(request):
    if request.method == "POST":
        myfile= request.FILES['file']
        fs = FileSystemStorage()   
        myfile = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(myfile)
        return render(request, 'user/upload.html',{
            'uploaded_file_url':uploaded_file_url
        }) 
    return render(request, 'user/upload.html')    
    
        
class CreateEletronicsWithFile(CreateView):
    print("CreateEletronicsWithFile")
    model = Eletronics
    template_name = 'user/upload.html'
    success_url ="/user/upload/"
    form_class = ElectronicsForm
    
    def form_valid(self, form):
        file = self.request.FILES['file']
        print(".........",file)
        return super().form_valid(form)
    
    #size 2 mb
    #type jpg png    
 

class GetEletronics(ListView):
    model = Eletronics
    template_name = 'user/eletronics.html'
    context_object_name = 'eletronics'
    #get_queryset(self):
    
    
        
class AddDocument(CreateView):
    model = Document        
    template_name = 'user/upload.html'
    form_class = DocumentForm
    success_url = '/user/upload/' 
    
    
    
    def form_valid(self, form):
        file = self.request.FILES['document']
        print(".........",file)
        return super().form_valid(form)
    
    

