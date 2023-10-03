from django.shortcuts import render
from django.views import generic

from website.models import Project


# Create your views here.
class ProjectsListView (generic.ListView):
    model = Project
