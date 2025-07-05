from django.urls import path
from .views import get_post_list, get_post_detail, create_post, login_view, \
    update_post  # Импортируем новое представление

urlpatterns = [
    path("posts/", get_post_list, name="post_list"),
    path('posts/<int:post_id>/', get_post_detail, name="post_detail"),
    path('posts/add/', create_post, name="new_post"),
    path('login/', login_view, name="login"),
    path('posts/<int:post_id>/edit/', update_post, name="update_post"),
]
