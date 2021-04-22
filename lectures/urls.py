from django.urls import path

from .views import LectureListView
from .views import LectureDetailView
from .views import LectureCreateView
from .views import LectureUpdateView
from .views import LectureDeleteView

app_name = 'lectures'

urlpatterns = [
    path('', LectureListView.as_view(), name='lecture-list'),
    path('<int:pk>', LectureDetailView.as_view(), name='lecture-detail'),
    path('create/', LectureCreateView.as_view(), name='lecture-create'),
    path('<int:pk>/update/', LectureUpdateView.as_view(), name='lecture-update'),
    path('<int:pk>/delete/', LectureDeleteView.as_view(), name='lecture-delete'),
]
