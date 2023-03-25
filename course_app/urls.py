from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='API Overview'),
    path('create/', views.create_course, name='Create Course'),
    path('list/', views.list_course, name='Search or List Courses'),
    path('update/<int:pk>/', views.update_course, name="Update Course"),
    path('delete/<int:pk>/', views.delete_course, name="Delete Course")
]
