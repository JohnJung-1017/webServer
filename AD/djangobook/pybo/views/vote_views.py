from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer

# 질문 추천 함수 개선
@login_required(login_url='common:login')
def vote_up_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        if request.user in question.voter.all():
            question.voter.remove(request.user)
            question.vote_count -= 1
        else:
            question.voter.add(request.user)
            question.vote_count += 1
        question.save()
    return redirect('pybo:detail', question_id=question.id)

# 질문 비추천 기능 추가
@login_required(login_url='common:login')
def vote_down_question(request, question_id):
    """
    pybo 질문비추천
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 비추천할 수 없습니다')
    else:
        if request.user in question.voter.all():
            question.voter.remove(request.user)
            question.vote_count += 1
        else:
            question.voter.add(request.user)
            question.vote_count -= 1
        question.save()
    return redirect('pybo:detail', question_id=question.id)

# 답변 추천 함수 개선
@login_required(login_url='common:login')
def vote_up_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        if request.user in answer.voter.all():
            answer.voter.remove(request.user)
            answer.vote_count -= 1
        else:
            answer.voter.add(request.user)
            answer.vote_count += 1
        answer.save()
    return redirect('pybo:detail', question_id=answer.question.id)

# 답글 비추천 기능 추가
@login_required(login_url='common:login')
def vote_down_answer(request, answer_id):
    """
    pybo 답글비추천
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 비추천할 수 없습니다')
    else:
        if request.user in answer.voter.all():
            answer.voter.remove(request.user)
            answer.vote_count += 1
        else:
            answer.voter.add(request.user)
            answer.vote_count -= 1
        answer.save()
    return redirect('pybo:detail', question_id=answer.question.id)
