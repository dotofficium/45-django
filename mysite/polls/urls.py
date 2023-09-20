from django.urls import path

from . import views

urlpatterns = [
    path("mypage/", views.show, name="my-page"),
    path("addition/<int:a>/<int:b>/", views.add, name="addition"),
    path("fact/<int:num>/", views.fact, name="fact"),
]
