from django.shortcuts import render, get_object_or_404,redirect
from .models import Question, Answer
from .forms import QuestionForm,AnswerForm
from django.core.paginator import Paginator
"""
페이지 나누기 - 사용자가 요청한 페이지 가져오기


"""


def index(request):
    # 질문 목록 

    # 페이지 나누기 - 사용자가 요청한 페이지 가져오기
    # http://127.0.0.1:8000/board/?ㅔㅁㅎㄷ=1
    # page = request.GET['page']
    page = request.GET.get('page')

    # select * from question
    # question_list = Question.objects.all()

    # select * from question order by created_at desc
    question_list = Question.objects.order_by("-created_at")

    paginator = Paginator(question_list,10)
    # pageinator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}

    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    # qid 조회
    # select * from question where id=qid
    # get_object_or_404(), get(), filter()

    question = get_object_or_404(Question, id=qid)

    context = {"question":question}

    return render(request, "board/question_detail.html", context)

def question_create(request):
    """
    질문등록
    get - 비어있는 QuestionForm 보내기
    post - QuestionForm 사용자 입력값 연결
    """
    if request.method == "POST":
        # 사용자 입력값 가져오기
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("board:index")
    else:
        form = QuestionForm()
    return render(request, "board/question_create.html",{"form":form})

def question_edit(request, qid):
    pass

def question_delete(request, qid):
    pass



################답변
def answer_create(request,qid):
    """
    답변등록
    1) question 을 이용해 답변 등록
    question.answer_set.create()

    2) insert into answer(content,qid) values('답변',1)
    question = get_object_or_404(Question,id=id)
    answer = Answer(question=question, content=request.POST[''])
    answer.save()
    """

    # form 사용하지 않는 방식
    # question = get_object_or_404(Question, id=qid)
    # save() 명령어 안해도 됨
    # question.answer_set.create(content=request.POST["content"])

    # form  사용방식
    question = get_object_or_404(Question, id=qid)
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.save() : commit 은 default 가 True 상태로 db 바로 반영
            answer = form.save(commit=False)
            # 어느 질문에 대한 답변인가?
            answer.question = question
            answer.save()
            return redirect("board:detail", qid=qid)    
    else:
        form = AnswerForm()
    context = {"question": question, "form":form}
    return render(request, "board/question_detail.html", context)
    

def answer_edit(request, aid):
    pass

def answer_delete(request, aid):
    pass
