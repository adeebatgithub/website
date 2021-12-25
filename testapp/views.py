from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm,signupform
# Create your views here.

def post_list(request):
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'testapp/post_list.html',{ 'posts' : posts })
    
def post_detail(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'testapp/post_details.html', {'post' : post})

#################

def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'testapp/post_edit.html', {'form':form})
    
def post_edit(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'testapp/post_edit.html', {'form':form})

#################################

def signup(request):
    
	if request.method == "POST":
		form = signupform(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect("login")
	else:
	    form = signupform()
	return render (request,'registration/signup.html',{'form':form})