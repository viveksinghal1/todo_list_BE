from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tasks/', views.allTasks, name="all-tasks"),
    path('tasks/<str:pk>/', views.specificTask, name="specific-task"),
]