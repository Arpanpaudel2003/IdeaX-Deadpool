from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

def home(request):
    return render(request,'home.html')

def map(request):
    return render(request, 'map.html')

def blog(request):
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