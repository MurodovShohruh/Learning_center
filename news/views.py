from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import News
from .serializers import NewsListSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['News'])
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = [AllowAny]