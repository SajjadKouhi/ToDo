from django.urls import path
from . views import *

urlpatterns = [
        path('register/' , RegisterUserView.as_view() , name = 'register'),
        path('login/' , LoginView.as_view() , name = 'login') , 
        path('tasks/', RegisterTasksView.as_view() , name = 'Tasks_Register') ,
        path('completed-tasks/<int:user_task_id>/' , CompletedTasksView.as_view() , name  = 'Tasks-Completed') ,
        path('Delete-tasks/<int:user_task_id>/',DeleteTasksView.as_view() , name='Deleted-Tasks') , 
        path('update-task/<str:user_task_id>/', UpdateTaskView.as_view(), name='update-task')
        ]