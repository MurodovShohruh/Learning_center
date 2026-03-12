from django.urls import path, include
from .views import NewsListView

urlpatterns = [
    path('news/', NewsListView.as_view(), name="news"),
]