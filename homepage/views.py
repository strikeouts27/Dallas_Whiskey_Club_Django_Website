from django.shortcuts import render

# Create your views here.
def homepageview(request):
    context = {
        'name': 'Dallas Whiskey Club',
    }
    return render(request, 'homepage.html', context)