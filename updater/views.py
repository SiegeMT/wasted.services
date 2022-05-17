from django.shortcuts import render

# Create your views here.
def updater(request):
    return render(request, 'updater/updater.html', {})
