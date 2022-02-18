from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from datetime import datetime


# Create your views here.

def index(request):
	date = datetime.now()
	day = date.strftime('%A')
	day_num = date.strftime('%d')
	post = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
	return render(request, 'Blogg/index.html', {
		'post': post,
		'day': day,
		'day_num': day_num
	})
