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
def sendMail(request):
    subject = 'Welcome to Project Management System'
    message = 'Thank you for registering with us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['samir.vithlani83955@gmail.com']
    res = send_mail(subject, message, email_from, recipient_list)
    print(res)
    return HttpResponse('Mail sent successfully')
    
    
        


