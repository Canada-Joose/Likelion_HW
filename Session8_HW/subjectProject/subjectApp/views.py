from django.shortcuts import render, redirect
from .models import Subject, Major
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.


class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')


class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')


class editSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')


class editMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')


def home(request):
    subjects = Subject.objects.all()
    majors = Major.objects.all()
    return render(request, 'home.html', {'subjects': subjects, 'majors': majors})


def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__name='컴퓨터학과')
    return render(request, 'computer.html', {'computerMajor': computerMajor})


def psychologySubjectView(request):
    subjects = Subject.objects.all()
    psychologyMajor = subjects.filter(major__name='심리학부')
    return render(request, 'psychology.html', {'psychologyMajor': psychologyMajor})


def deleteSubjectView(reqeust, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')


def deleteMajortView(reqeust, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')
