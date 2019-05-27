from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='job-home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('about/', views.about, name='job-about'),
	path('apply/', views.apply, name='job-apply'),
	path('announcement/', views.announcement, name='job-announcement'),

]