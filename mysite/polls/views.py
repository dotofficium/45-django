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


from django.http import HttpResponseRedirect
from django.urls import reverse
def create_student(request):
    if request.method == "POST":
        # ipdb> request.method
        # 'POST'
        # ipdb> request.POST
        # <QueryDict: {'csrfmiddlewaretoken': ['x7wnDLuBGJwgbqDFgxwm1sHv5SPIfmNK0ae0rsl1UsLtJygt4wDgfI7vqATe1eh6'],
        # 'first_name': ['Mahesh'], 'last_name': ['Kumar'],
        # 'email': ['mahesh@gmail.com'], 'dob': ['1998-03-38'],
        # 'mobile': ['1234567890'], 'gender': ['male']}>
        # ipdb> request.POST["mobile"]
        # '1234567890'
        # import ipdb;ipdb.set_trace()
        student = Student.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            dob=request.POST["my-dob"],
            mobile=request.POST["mobile"],
            gender=request.POST["gender"]
        )
        return HttpResponseRedirect(reverse("polls:student-list", args=[]))
    else:
        return render(
            request,
            template_name="si/create_student.html",
            context={})


