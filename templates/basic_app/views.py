from django.shortcuts import render


# Create your views here.

def index(request):
    content_dict = {'text':'hello ssdd world', 'number':100}
    return render(request,'basic_app/index.html', context = content_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/rel_url_temps.html')
