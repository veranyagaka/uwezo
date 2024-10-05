from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile',views.profiles_view, name='profile'),
    
    #path('profile/<str:username>/', views.profiles_view, name='profiles'), # other peoples profiles
    path('trending/', views.trending_posts, name='trending_posts'),
    path('recent/', views.recent_posts, name='recent_posts'),
    path('map/', views.map_view, name='map_view'),
    path('users/', views.user_list, name='user_list'),
    path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),
# add profile with image to look good
]