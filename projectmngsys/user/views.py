from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import TeacherSignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView,LogoutView

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
    
class LoginView(LoginView):
    
    template_name = 'user/login.html'
    
    def get(self, request, *args, **kwargs):
        print(self.request.user)
        # if self.request.user.is_teacher:
        #     print('teacher')
        # else:
        #     print('student')    
        return self.render_to_response(self.get_context_data())


