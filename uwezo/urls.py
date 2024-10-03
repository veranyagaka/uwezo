from django.urls import path
from . import views

# Inserted by Osborn
from .views import (
    RelationshipListCreateView, RelationshipDetailView,
    PostListCreateView, PostDetailView,
    LikeListCreateView, LikeDetailView,
    CommentListCreateView, CommentDetailView
)
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('map/', views.map_view, name='map_view'),
    path('users/', views.user_list, name='user_list'),
    path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),
# add profile with image to look good

# # Relationship URLs
    path('relationships/', RelationshipListCreateView.as_view(), name='relationship-list-create'),
    path('relationships/<int:pk>/', RelationshipDetailView.as_view(), name='relationship-detail'),

    # Post URLs
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Like URLs
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),

    # Comment URLs
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]