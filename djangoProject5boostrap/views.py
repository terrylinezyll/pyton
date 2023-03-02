from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def blog(request ):
    return render(request, 'blog.html')
def about(request ):
    return render(request,'about.html')
def contact(request ):
    return render(request,'contact.html')
def client(request ):
    return render(request,'client.html')
def services(request ):
    return render(request,'services.html')