from django.shortcuts import render

from django.http import HttpResponse


def show(request):
    return HttpResponse("I am in show page")


def add(request, a, b):
    return HttpResponse(f"Addition of two number {a} + {b} = {a + b}")


def fact(request, num):
    from functools import reduce
    return HttpResponse(f"fact of {num}: {reduce(lambda x, y: x * y, range(1, num+1))}")
