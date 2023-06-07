from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),

    # url za svaki post
    path('<slug:post>/', views.post_single, name='post_single'),

]