from django.urls import path

from .views import CourseCreateView
from .views import CourseDeleteView
from .views import CourseDetailView
from .views import CourseListView
from .views import CourseUpdateView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
