from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('about/', views.aboutfunction, name='about-page'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

]