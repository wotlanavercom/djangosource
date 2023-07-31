from .models import Question, Answer,Comment
from django import forms

"""
django - 화면 디자인 처리
1. html : 일반적인 처리(bootstrap 이용, 직접 디자인)
2. 장고의 form 클래스 이용
   forms.ModelForm, forms.Form 클래스를 상속받고 작성
"""


# class NameForm(forms.Form):
#     # 화면에 보여줄 요소
#     name = forms.CharField(
#         label="name", max_length=100, error_messages={"required": "이름입력"}
#     )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
