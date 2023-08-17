from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from  django.shortcuts import render
from  .models import Post,Category
def home(request):
    #load all the post from db
     posts=Post.objects.all()[:11]
     #print(posts)
     cats=Category.objects.all()

     data={
       'posts':posts,
         'cats':cats
     }
     return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request,'posts.html',{'post':post,'cat':cats})