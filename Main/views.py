from django.shortcuts import render

from .models import *
# Create your views here.

def MainPage(request):
	owner = Owner.objects.filter(name="Mario Malak").first()
	projects = Project.objects.all()
	
	context = {
		"owner":owner,
		"projects": projects, 
	}
	return render(request, "index.html", context)
