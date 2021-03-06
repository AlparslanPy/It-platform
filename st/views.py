from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project, Student

# Create your views here.


# @login_required
def index(request):
    student = Student.objects.all()
    project = Project.objects.all()
    context = {
        'student' : student,
        'project' : project
    }
    return render(request, 'st/index.html', context)

def students(request):
    project = Project.objects.all()
    context = {
        'project':project,
    }
    return render(request, 'st/students.html', context)

def projects(request, project_id):
    project = Project.objects.get(id=project_id)
    student = Student.objects.filter(project=project)
    context = {
        'project' : project,
        'student': student
    }
    return render(request, 'st/project.html', context)
