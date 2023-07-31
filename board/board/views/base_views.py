from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator


"""
페이지 나누기
Paginator 클래스
Paginator(전체리스트, 페이지당 보여줄개수)

has_previous : 이전 페이지 유무
has_next : 다음 페이지 유무

previous_page_number : 이전 페이지 번호
next_page_number : 다음 페이지 번호
number : 현재 페이지 번호
page_range : 페이지 범위
count : 전체 게시물 개수
start_index : 현재 페이지 인덱스(1부터 시작)
"""


def index(request):
    # 질문 목록

    # 페이지 나누기 - 사용자가 요청한 페이지 가져오기
    # http://127.0.0.1:8000/board/?page=1
    # page = request.GET['page']
    page = request.GET.get("page", 1)

    # select * from question
    # question_list = Question.objects.all()

    # select * from question order by created_at desc
    question_list = Question.objects.order_by("-created_at")

    paginator = Paginator(question_list, 10)
    # pageinator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}

    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    # qid 조회
    # select * from question where id=qid
    # get_object_or_404(), get(), filter()
    question = get_object_or_404(Question, id=qid)
    # question = Question.objects.get(id=qid)

    context = {"question": question}

    return render(request, "board/question_detail.html", context)

