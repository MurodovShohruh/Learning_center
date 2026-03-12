from django.urls import path
from .views import *

urlpatterns = [
    path('instructor/', InstructorListView.as_view()),
    path('instructor/<int:pk>/', InstructorDetailView.as_view()),

    path('instructor/create/', InstructorCreateView.as_view()),
    path('instructor/<int:pk>/update/', InstructorUpdateView.as_view()),
    path('instructor/<int:pk>/delete/', InstructorDeleteView.as_view()),
]