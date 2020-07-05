from django.shortcuts import render
from cooking.models import Recent,Activity
from django.http import HttpResponseRedirect

from cooking.forms import ContactForm
# Create your views here.

def index(request):

	recent = Recent.objects.all().order_by('-created')
	activity = Activity.objects.all().order_by("-created")
	form = ContactForm()
	return render(request, 'cooking/index.html',{'recent':recent, 'activity':activity,'form':form})


def submit(request):

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			form.save()
			print("Form is valid")
		else:
			print("Form is invalid  ")


	return HttpResponseRedirect('/#contact')