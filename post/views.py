from django.shortcuts import get_object_or_404, render ,redirect
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required
def post_create(request):
    if request.method == 'POST':
        form  = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()        
    else:
        form = PostCreateForm(data=request.GET)
    return render(request,'post/create.html',{'form':form})  

def feed(request):
    posts = Post.objects.all()
    logged_user = request.user
    return render(request,'post/feed.html',{'posts':posts,'logged_user':logged_user}) 
      
def like_post(request):   
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post,id=post_id)        
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')    
        
            
            
            

