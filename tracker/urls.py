from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('<str:short_code>/', views.user_progress, name='user_progress'),
    path('<str:short_code>/<int:user_id>/', views.user_progress, name='user_progress'),
]
