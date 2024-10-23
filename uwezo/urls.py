from django.urls import path
from . import views
from mpesa.views import mpesa_callback, mpesa, process_payment
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
    
    path('contribution/', views.recent_posts, name='contribution'),
    path('hotspot/', views.recent_posts, name='hotspot'),
    path('resource/', views.recent_posts, name='resource'),
    path('community/', views.recent_posts, name='community'),

    path('about/', views.recent_posts, name='about'),

    path('map/', views.map_view, name='map_view'),
    path('users/', views.user_list, name='user_list'),
    path('follow/<int:user_id>/', views.follow_unfollow, name='follow_unfollow'),

    path('callback/', mpesa_callback, name='mpesa_callback'),

    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/share/', views.share_post, name='share_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('mpesa/', mpesa, name='mpesa'),
    path('process_payment/', process_payment, name='process_payment'),
# add profile with image to look good
]