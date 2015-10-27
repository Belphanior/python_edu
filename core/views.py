from django.http.response import HttpResponse
from django.shortcuts import render

from core.models import Student


def main(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})