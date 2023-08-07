from django.urls import path
from .views import TodosApiZiew

urlpatterns = [
    # 클레스로 작성된 뷰 사용시 as_view() 무조건 사용
    path("", TodosApiZiew.as_view(),name="todo"),
]
