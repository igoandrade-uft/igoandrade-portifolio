from django.shortcuts import render
from apps.projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
