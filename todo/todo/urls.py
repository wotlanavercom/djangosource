from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/todo/
    path("",views.todo_list, name="todo_list"),
    # http://127.0.0.1:8000/todo/1/
    path("<int:id>/",views.todo_detail, name="todo_detail"),
    # http://127.0.0.1:8000/todo/new/
    path("new/", views.todo_create, name="todo_create"),
    # http://127.0.0.1:8000/todo/1/edit     수정
    path("<int:id>/edit/", views.todo_edit, name="todo_edit"),
    # http://127.0.0.1:8000/todo/done/1/     완료
    path("done/<int:id>/", views.todo_done, name="todo_done"),
    # http://127.0.0.1:8000/todo/done/       완료된 목록 보기
    path("done/", views.done_list, name="done_list"),
]
