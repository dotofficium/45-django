from django.urls import path

from . import views
app_name = "polls"

urlpatterns = [
    path("mypage/", views.show, name="my-page"),
    path("addition/<int:a>/<int:b>/", views.add, name="addition"),
    path("fact/<int:num>/", views.fact, name="fact"),
    path("data/", views.data_rendering, name="my-data-render"),

    # Question and choice
    path("question/list/", views.questions_list, name="question-list"),
    path("question/detail/<int:pk>/", views.question_detail, name="question-detail"),

    path("students/list/", views.students_list, name="student-list"),
    path("students/detail/<int:pk>/", views.student_detail, name="students-detail"),
    path("students/create/", views.create_student, name="create-student")
]