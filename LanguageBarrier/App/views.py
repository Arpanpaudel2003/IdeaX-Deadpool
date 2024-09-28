from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def home(request):
    return render(request,'home.html')

def map(request):
    return render(request, 'map.html')

from django.shortcuts import render, redirect
from .models import Post  # Make sure to import your Post model
from .forms import PostForm  # Import your form

def blog(request):
    # Get the search query from GET parameters
    search_query = request.GET.get('search', '')
    
    # Filter posts based on the search query if provided
    if search_query:
        posts = Post.objects.filter(para__icontains=search_query)  # Adjust to your field
    else:
        posts = Post.objects.all()
    
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/blog")
    
    context = {'posts': posts, 'form': form, 'search_query': search_query}
    return render(request, 'blog.html', context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/blog")
    
    context = {'form': form}
    return render(request, "update_post.html", context)

def deletePost(request, pk):
    item = Post.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('/blog')
    
    context = {'item': item}
    return render(request, 'delete.html', context)
        

def currency(request):
    return render(request,'currency.html')

def translate(request):
    return render(request,'translate.html')