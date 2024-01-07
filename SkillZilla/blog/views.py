from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.core.paginator import Paginator

from .forms import *
from .models import Project


def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comm = form.save()
            return redirect('home')
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    paginator = Paginator(comments, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', context={'form': form, 'page_obj': page_obj})


def about(request):
    return render(request, 'blog/about.html')


def stack(request):
    return render(request, 'blog/stack.html')


def projects(request):
    proj = Project.objects.all()
    return render(request, 'blog/projects.html', context={'projects': proj})


def contact(request):
    return render(request, 'blog/contact.html')


def details(request, slug):
    proj = Project.objects.get(slug=slug)
    return render(request, 'blog/details.html', context={'proj': proj})


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'blog/detailProject'
