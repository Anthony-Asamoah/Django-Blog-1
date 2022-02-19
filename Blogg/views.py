from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from datetime import datetime
from .forms import PostForm

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


def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.date_published = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
		else:
			form = PostForm
			return render(request, 'Blogg/edit_post.html', {
				'form': form,
				'day': day,
				'day_num': day_num
			})

	form = PostForm
	return render(request, 'Blogg/edit_post.html', {
		'form': form,
		'day': day,
		'day_num': day_num
	})


def edit_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'Blogg/edit_post.html', {'form': form,
        'day': day,
        'day_num': day_num
    })
