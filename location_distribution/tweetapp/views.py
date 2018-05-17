from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	my_dict = { 'insert_me': 'Hellooooooooooo I am from django file'}
	return render(request, 'tweetapp/index.html', context=my_dict)
