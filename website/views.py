from django.shortcuts import render
from .models import Experience

# Create your views here.
def home(request):
	experiences = Experience.objects
	return render(request, 'home.html', {'website':experiences})

