from django.shortcuts import render
from django.views.generic import TemplateView
from .models import posts
class PostsHome(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'posts/home.html',{})

class Posts(TemplateView):

    def get(self, request, *args, **kwargs):
        allposts = posts.objects.all()
        return render(request,'posts/allposts.html',{'allposts':allposts})