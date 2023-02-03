from django.urls import path
from .views import BlogListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_update'),
    path('post/new', BlogCreateView.as_view(), name = 'post_entry'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name = 'post_delete'),
]
