from django.shortcuts import render

# Create your views here.
def homeview(request):
    context = {
        'name': 'Dallas Whiskey Club',
    }
    return render(request, 'homepage/home.html')