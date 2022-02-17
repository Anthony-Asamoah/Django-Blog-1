from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone


# Create your views here.

def index(request):
	post = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
	return render(request, 'Blogg/index.html', {
		'post': post
	})
