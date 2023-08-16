from django.urls import path
from first_app.views import add_Task, show_tasks, edit_task, delete_task, completed_tasks, complete_task

urlpatterns = [
    path('', add_Task, name='add_task'),
    path('show_tasks/', show_tasks, name='show_tasks'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('completed_tasks/<int:id>', complete_task, name='complete_task'),
    path('completed_tasks/', completed_tasks, name='completed_tasks'),
]
