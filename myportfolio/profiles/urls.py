from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('profiles/', views.add_user_profile ,name="add_user_profile"),
    path('user/<str:name>/', views.user_profile ,name="user_profile")
]
