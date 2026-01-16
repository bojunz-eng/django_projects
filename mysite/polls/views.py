from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader

from .models import Question


def index(request):
    # return HttpResponse("Hello world. 816751b2 You're at the polls index now.")

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list, "owner": "816751b2"}
    return render(request, "polls/index.html", context)

def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. 816751b2 is the polls index.")
    return response


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    """
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, "polls/detail.html", {"question": question})
    """

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
