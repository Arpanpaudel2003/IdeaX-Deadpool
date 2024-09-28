<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
=======
from django.shortcuts import render
from django.http import JsonResponse
import requests
>>>>>>> a32c93576d72888ee63409c5195eb2624417066e


def home(request):
    return render(request,'home.html')

def map(request):
    return render(request, 'map.html')

from django.shortcuts import render, redirect
from .models import Post  # Make sure to import your Post model
from .forms import PostForm  # Import your form

def blog(request):
<<<<<<< HEAD
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
=======
    return render(request,'blog.html')

def translate(request):
    if request.method == 'POST':
        source_lang = request.POST.get('sourceLang')
        target_lang = request.POST.get('targetLang')
        input_text = request.POST.get('inputText')

        # Call OpenAI API for translation
        headers = {
            'Authorization': f'Bearer YOUR_OPENAI_API_KEY',
            'Content-Type': 'application/json',
        }
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{
                'role': 'user',
                'content': f'Translate the following text from {source_lang} to {target_lang}: "{input_text}"'
            }]
        }

        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

        if response.status_code == 200:
            translated_text = response.json()['choices'][0]['message']['content']
            return JsonResponse({'translatedText': translated_text})
        else:
            return JsonResponse({'error': 'Translation failed'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
>>>>>>> a32c93576d72888ee63409c5195eb2624417066e
