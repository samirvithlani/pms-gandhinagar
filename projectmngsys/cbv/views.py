from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
#Gnericview ---> django.views.generic

class CreatePost(CreateView):
    model = Post
    fields = ['title','body','date','time','genere']
    template_name = 'cbv/create.html'
    success_url = '/cbv/list'