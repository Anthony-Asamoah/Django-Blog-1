from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from datetime import datetime

# Create your views here.
date = datetime.now()
day = date.strftime('%A')
day_num = date.strftime('%d')


def index(request):
	post = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
	return render(request, 'Blogg/index.html', {
		'post': post,
		'day': day,
		'day_num': day_num
	})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'Blogg/post_details.html', {
		'post': post,
		'day': day,
		'day_num': day_num
	})
