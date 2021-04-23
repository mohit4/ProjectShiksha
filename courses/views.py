from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Course


class CourseListView(ListView):
    """
    Listing all the courses
    """
    template_name = 'courses/course_list.html'
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    """
    Details of a course
    """
    template_name = 'courses/course_detail.html'
    model = Course
    context_object_name = 'course'


class CourseCreateView(SuccessMessageMixin, CreateView):
    """
    Creating a new course
    """
    template_name = 'courses/course_create.html'
    model = Course
    fields = ('title', 'description', 'syllabus')
    success_message = 'New course created!'


class CourseUpdateView(SuccessMessageMixin, UpdateView):
    """
    Updating a new course
    """
    template_name = 'courses/course_update.html'
    model = Course
    fields = ('description', 'syllabus')
    success_message = 'Course updated!'


class CourseDeleteView(DeleteView):
    """
    Deleting an existing course
    """
    template_name = 'courses/course_detail.html'
    model = Course
    success_url = reverse_lazy('homepage')
