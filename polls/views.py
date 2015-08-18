from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
# Mode 3)
#from django.template import RequestContext, loader
# Mode 6)
from django.http import Http404
from django.shortcuts import render

from .models import Question

def index(request):
    # 1) Simple Message
    #return HttpResponse("Hello, world. You're at the polls index.")
    # 3) Database query
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([p.question_text for p in latest_question_list])
    #return HttpResponse(output)
    # 4) Database query with template
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))
    # 5) Database query with render
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    
def detail(request, question_id):
    # 2) Simple Message
    # return HttpResponse("You're looking at question %s." % question_id)
    # 6) Message that Raises a 404 error if the requested ID doesn’t exist
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})
    # 7) Shortcut – get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)