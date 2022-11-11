from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list' ),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail' ),
    path('comment/<int:post_id>/', views.PostCommentCreateView.as_view(), name='comment_create' ),
    path('create/', views.BlogCreateView.as_view(), name='blog_create' ),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update' ),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete' ),
]
