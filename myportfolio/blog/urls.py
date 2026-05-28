from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_post, name="add_post"),
    path('delete/<int:id>/', views.delete_post, name="delete_post"),
    path('update/<int:id>/', views.update_post, name="update_post"),
]
