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