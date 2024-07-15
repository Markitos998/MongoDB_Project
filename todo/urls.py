from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllToDos.as_view(), name='index'),
    path('today/', views.TodayToDos.as_view(), name='today'),
    path('create/', views.CreateToDoItem.as_view(), name='create_todo'),
    path('update/<str:pk>/', views.UpdateToDoItem.as_view(), name='update_todo'),
    path('delete/<str:pk>/', views.DeleteToDoItem.as_view(), name='delete_todo'),
]
