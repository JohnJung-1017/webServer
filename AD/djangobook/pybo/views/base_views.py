from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    search_query = request.GET.get('q', '')  # 검색어

    # 검색 기능 추가 구현
    if search_query:
        question_list = Question.objects.filter(
            Q(subject__icontains=search_query) |
            Q(content__icontains=search_query)
        ).select_related('author').order_by('-create_date')
    else:
        question_list = Question.objects.select_related('author').order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'search_query': search_query}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
