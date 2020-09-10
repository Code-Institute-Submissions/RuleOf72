from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.

def show_forum(request):
    return render(request, 'forum.template.html')