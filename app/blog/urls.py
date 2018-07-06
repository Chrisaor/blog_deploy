from django.urls import path

from blog import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('about/', views.about, name='about'),
    path('post_add/', views.post_add, name='post_add')
]