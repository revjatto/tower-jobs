from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Post


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'job/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'job/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
   
class PostDetailView(DetailView):
    model = Post	

def about(request):
	return render(request, 'job/about.html')

def apply(request):
	return render(request, 'job/apply.html')

@login_required
def announcement(request):
	return render(request, 'job/announcement.html')

