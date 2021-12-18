from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def punejobsinfo(request):
    return render(request,'testapp/news.html')
def sportsinfo(request):
    return render(request,'testapp/news.html')
