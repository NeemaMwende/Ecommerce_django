from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
    # return HttpResponse("<h1 style=color: purple>Our web progress </h1>")