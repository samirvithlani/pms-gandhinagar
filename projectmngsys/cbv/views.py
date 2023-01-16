from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#Gnericview ---> django.views.generic

class CreatePost(CreateView):
    model = Post
    fields = ['title','body','date','time','genere']
    template_name = 'cbv/create.html'
    success_url = '/cbv/list'

# @login_required
@method_decorator(login_required, name='dispatch')
class ListAllPost(ListView):
    #context ={}
    model = Post
    template_name = 'cbv/list.html'
    #post = Post.objects.all()
    #context [''] = 'posts'
    context_object_name = 'posts' 
    
class PostDetail(DetailView):
    model = Post
    template_name = 'cbv/detail.html'
    context_object_name = 'post'    

class PostDelete(DeleteView):
    model = Post
    template_name = 'cbv/delete.html'
    success_url = '/cbv/list'
    
class UpdatePost(UpdateView):
    model = Post
    template_name = 'cbv/update.html'
    fields = '__all__'
    success_url = '/cbv/list'