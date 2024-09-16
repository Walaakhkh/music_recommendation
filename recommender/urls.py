from django.urls import path
from . import views

urlpatterns = [
    path('recommend/<int:user_id>/', views.recommend_view, name='recommend'),
]
