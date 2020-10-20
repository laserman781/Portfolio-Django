from django.shortcuts import render
from .models import Experience

# Create your views here.
def home(request):
	experience = Experience.objects
	return render(request, 'home.html', {'experience':experience})

