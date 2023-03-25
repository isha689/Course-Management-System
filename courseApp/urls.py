from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApiOverview , name = 'API Overview'),
    path('create/', views.CreateCourse, name = 'Create Course'),
    path('list/', views.ListCourse, name = 'Search or List Courses'),
    path('update/<int:pk>/', views.UpdateCourse, name = "Update Course"),
    path('delete/<int:pk>/', views.DeleteCourse, name = "Delete Course")
]