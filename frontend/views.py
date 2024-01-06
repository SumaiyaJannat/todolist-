from django.shortcuts import render
import requests

# Create your views here.

def list(request):
	return render(request, 'frontend/task_form.html')



        