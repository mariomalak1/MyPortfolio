from django.shortcuts import render, redirect
# from .forms import TagForm
# from .models import *
# import json
# Create your views here.

def MainPage(request):
	owner = Owner.objects.filter(name="Mario Malak").first()
	projects = Project.objects.all()
	
	context = {
		"owner":owner,
		"projects": projects, 
	}
	return render(request, "index.html", context)

def create_tag(request):
	if request.method == "POST":
		form = TagForm(request.POST)
		
		num = int(request.POST.get('form_count', 1))

		print(num)

		for i in range(1, num + 1):
			form_prefix = f"form_{i}"
			form = FormModelForm(request.POST, prefix=form_prefix)

			if form.is_valid():
				form.save()   # Save the form data to the database
				redirect("create_tag")
	else:
		form = TagForm(prefix='form_1')
	context = {
		"form": form, 
	}

	return render(request, "add_tag.html", context)

'''
def save_tag(request):
	if request.method == "POST":
		try:
            data = json.loads(request.tags)
            # Work with the JSON data here
        except json.JSONDecodeError:
            # Handle JSON decoding error if necessary
            return HttpResponseBadRequest("Invalid JSON data")
	else:
		# Handle other request methods or return an error response
        return HttpResponseNotAllowed(['POST'])


def my_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Work with the JSON data here
        except json.JSONDecodeError:
            # Handle JSON decoding error if necessary
            return HttpResponseBadRequest("Invalid JSON data")
    else:
        # Handle other request methods or return an error response
        return HttpResponseNotAllowed(['POST'])
'''
