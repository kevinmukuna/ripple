from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('about/', views.aboutfunction, name='about-page'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('dashboard', views.dashboardfunction, name="dashboard"),
    path('dashboard/function', views.dashboard_user_functionality, name="function"),
    path('dashboard/post', UserPostListView.as_view(), name='dashboard-post')

]
