from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, posts_of_following_profiles
from . import views


urlpatterns = [
   path('', posts_of_following_profiles, name='index'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('post/new/', PostCreateView.as_view(), name='post_create'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
   path('about/', views.about, name='about'),

]
