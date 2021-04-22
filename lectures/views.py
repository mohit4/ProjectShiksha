from datetime import datetime

from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Lecture


class LectureListView(ListView):
    """
    Listing all the lectures in the system
    """
    template_name = 'lectures/lecture_list.html'
    model = Lecture
    context_object_name = 'lectures'


class LectureDetailView(DetailView):
    """
    Putting detail view of a specific lecture
    """
    template_name = 'lectures/lecture_detail.html'
    model = Lecture
    context_object_name = 'lecture'


class LectureCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new lecture
    """
    template_name = 'lectures/lecture_create.html'
    model = Lecture
    fields = ('title', 'description', 'video_link', 'content_files')
    success_message = 'New lecture created!'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        print(f'Form : {form}')
        return super().form_valid(form)


class LectureUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating an existing lecture
    """
    template_name = 'lectures/lecture_update.html'
    model = Lecture
    fields = ('title', 'description', 'video_link', 'content_files')
    success_message = 'Lecture updated!'


class LectureDeleteView(DeleteView):
    """
    Deleting an existing lecture from the system
    """
    template_name = 'lectures/lecture_detail.html'
    model = Lecture
    success_url = reverse_lazy('homepage')