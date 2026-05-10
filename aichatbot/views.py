from django.shortcuts import render

def index(request):
    return render(request, 'aichatbot/ai_chat.html')