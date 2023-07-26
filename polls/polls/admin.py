from django.contrib import admin
from .models import Question, Choice

# admin.site.register(Question)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields 에 정의한 순서대로 화면에 보여지게 됨
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date")

admin.site.register(Question, QuestionAdmin)
