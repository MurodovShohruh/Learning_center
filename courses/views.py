from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Course
from .serializers import CourseSerializers
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Courselar'])
class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [AllowAny]