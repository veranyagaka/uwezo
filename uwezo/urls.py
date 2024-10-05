from django.urls import path
from . import views
from mpesa.views import mpesa_callback
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile',views.profiles_view, name='profile'),
    path('report-incident/', views.report_incident, name='report_incident'),

    path('track-progress/', views.track_progress, name='track_progress'),

    #path('profile/<str:username>/', views.profiles_view, name='profiles'), # other peoples profiles
    path('trending/', views.trending_posts, name='trending'),
    path('recent/', views.recent_posts, name='recent'),
    path('map/', views.map_view, name='map_view'),
    path('users/', views.user_list, name='user_list'),
    path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),

    path('callback/', mpesa_callback, name='mpesa_callback')
# add profile with image to look good
]