from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    """
    forms 모듈에 선언된 ModelForm 클래스 상속받은 TodoForm 작성
    Todo 모델과 TOdoForm은 연결된 상태 : form 작업 시 모델에 반영
    """
    class Meta:
        """
        반드시 존재해야 함
        Todo 모델 기반의 폼, 모델에서 작성된 필드 중에서 일부 사용
        """
        model = Todo
        fields = ["title","description", "important"]
