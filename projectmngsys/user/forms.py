from django.contrib.auth.forms import UserCreationForm
from .models import User,Student
from django.db import transaction
from django import forms
from .models import Eletronics,Document

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =("username","email","password1","password2","degree")
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        return user    

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =("username","email","password1","password2","mobile")
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user    
        

class ElectronicsForm(forms.ModelForm):
    class Meta:
        model = Eletronics
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )        
        
            