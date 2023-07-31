from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Question, Answer
from ..forms import AnswerForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages




##################### 답변
@login_required(login_url="users:login")
def answer_create(request, qid):
    """
    답변등록
    1) question 을 이용해 답변 등록
    question.answer_set.create()

    2) insert into answer(content,qid) values('답변',1)
    question = get_object_or_404(Question,id=qid)
    answer = Answer(question=question,content=request.POST[''])
    answer.save()
    """

    # form 사용하지 않는 방식
    # question = get_object_or_404(Question, id=qid)
    # save() 명령어 안해도 됨
    # question.answer_set.create(content=request.POST["content"])

    # form 사용방식
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.save() : commit 은 default 가 True 상태로 db 바로 반영
            answer = form.save(commit=False)
            # 어느 질문에 대한 답변인가?
            answer.question = question
            answer.author = request.user
            answer.save()
            # return redirect("board:detail", qid=qid)
            # detail 앵커 이용
            return redirect("{}#answer_{}".format(resolve_url("board:detail",qid=qid), answer.id))
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


@login_required(login_url="users:login")
def answer_edit(request, aid):
    """
    get : 수정 화면 보여주기
          수정 답변 찾기 => 수정 답변 폼과 연결하기
    post : 답변 수정
           수정 성공 시 detail 이동
    """

    answer = get_object_or_404(Answer, id=aid)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            # return redirect("board:detail", qid=answer.question_id)
            return redirect("{}_#answer{}".format(resolve_url("board:detail", qid=answer.question_id),answer.id))
    else:
        form = AnswerForm(instance=answer)

    return render(request, "board/answer_edit.html", {"form": form})


def answer_delete(request, aid):
    """
    답변 삭제 후 detail 이동
    """
    answer = get_object_or_404(Answer, id=aid)
    answer.delete()

    # qid = answer.question_id(테이블 필드명 이용)
    # qid = answer.question.id
    return redirect("board:detail", qid=answer.question.id)

# 답변 추천
@login_required(login_url="users:login")
def vote_answer(request,aid):
    # question 찾기
    answer = get_object_or_404(Answer,id=aid)

    # 로그인 사용자와 질문작성자가 동일할 때 본인이 작성한 글은 추천 불가 라는 메세지 보여주기
    if request.user == answer.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        # 추천 user 추가
        answer.voter.add(request.user)
    # detail 이동
    return redirect("board:detail", qid=answer.question.id)