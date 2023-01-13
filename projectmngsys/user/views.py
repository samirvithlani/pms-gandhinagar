from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import TeacherSignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect

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
    

    