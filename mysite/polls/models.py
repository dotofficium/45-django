from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.question_text}-{self.choice_text}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Interview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) # HCL software Trinee
    mode = models.CharField(max_length=20) # online or offline
    sub_mode = models.CharField(max_length=20) # mock. group, exeam
    marks = models.FloatField()
    max_marks = models.IntegerField(default=100)
    result = models.CharField(max_length=10) # pass, not-clear

    def __str__(self):
        return f"{self.student.first_name}-{self.name}-{self.result}"

"""   
from polls.models import Student, Interview
s1 = Student.objects.get(id=1)
s2 = Student.objects.get(id=2)
Student.objects.create(
    first_name="suresh", 
    last_name="kumar", 
    email="suresh@example.com", 
    dob="1995-08-25", 
    mobile="9087654321", 
    gender="male"
)
s1.interview_set.create(name="HCL campus drive", mode="offline", sub_mode="interview", marks=60.5, result="pass")
s1.interview_set.create(name="Wipro campus drive", mode="Online", sub_mode="interview", marks=60.5, result="fail")
s1.interview_set.create(name="DELL campus drive", mode="offline", sub_mode="mock", marks=60.5, result="pass")

Interview.objects.create(student=s2, name="Wipro campus drive", mode="Online", sub_mode="mock", marks=60.5, result="pass")
Interview.objects.create(student=s2, name="DELL campus drive", mode="offline", sub_mode="mock", marks=60.5, result="fail")
Interview.objects.create(student=s2, name="LNT campus drive", mode="offline", sub_mode="mock", marks=60.5, result="pass")

"""