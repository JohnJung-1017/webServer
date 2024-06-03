from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Question, Answer, Comment

@login_required(login_url='common:login')
def my_page(request):
    user = request.user
    questions = Question.objects.filter(author=user).order_by('-create_date')
    answers = Answer.objects.filter(author=user).order_by('-create_date')
    comments = Comment.objects.filter(author=user).order_by('-create_date')
    
    context = {
        'questions': questions,
        'answers': answers,
        'comments': comments,
    }
    return render(request, 'pybo/my_page.html', context)
