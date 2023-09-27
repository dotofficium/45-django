from django.shortcuts import render

from django.http import HttpResponse


def show(request):
    return HttpResponse("I am in show page")


def add(request, a, b):
    return HttpResponse(f"Addition of two number {a} + {b} = {a + b}")


def fact(request, num):
    from functools import reduce
    return HttpResponse(f"fact of {num}: {reduce(lambda x, y: x * y, range(1, num+1))}")


def data_rendering(request):
    data = [
        {"gender": "male", "first_name": "suresh", "last_name": "kumar", "age": 25,
         "tech": ["python", "django", "selenium"]},
        {"gender": "female", "first_name": "sandya", "last_name": "kumari", "age": 25, "tech": ["Java", "springs"]},
        {"gender": "male", "first_name": "suresh", "last_name": "kumar", "age": 25,
         "tech": ["python", "django", "selenium"]},
        {"gender": "female", "first_name": "keerthi", "last_name": "yadav", "age": 25, "tech": ["c", "networks", "linux"]},
        {"gender": "female", "first_name": "taja", "last_name": "aswani", "age": 25, "tech": [".net", "c#", "powerBI"]}
    ]
    return render(request, template_name="render.html", context={"mydata": data})


# ************************** Questions and Choice models ******************

# list                  :
# detail - individual   : unque key, primary key
# Add
# update
# delete

from .models import Question, Choice
from django.shortcuts import get_object_or_404


def questions_list(request):
    questions = Question.objects.all()
    return render(request, template_name="qc/questions.html",
                  context={"questions": questions})


"""
In [6]: question = Question.objects.get(id=1)
In [7]: question
Out[7]: <Question: how are you?>
In [8]: Choice.objects.filter(question=question)
Out[8]: <QuerySet [<Choice: how are you?-good>]>
In [9]: question.choice_set.create(choice_text="fine", votes=100)
Out[9]: <Choice: how are you?-fine>
In [10]: Choice.objects.filter(question=question)
Out[10]: <QuerySet [<Choice: how are you?-good>, <Choice: how are you?-fine>]>
In [11]: question.choice_set.all()
Out[11]: <QuerySet [<Choice: how are you?-good>, <Choice: how are you?-fine>]>
"""


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, template_name="qc/detail_question.html",
                  context={"question": question})


from .models import Student, Interview
def students_list(request):
    students = Student.objects.all()
    return render(request, template_name="si/students.html", context={"students": students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, template_name="si/detail_student.html",
                  context={"student": student})


