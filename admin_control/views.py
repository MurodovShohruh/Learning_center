from rest_framework import viewsets, permissions
from instructor.serializers import InstructorSerializer
from instructor.models import Instructor
from courses.serializers import CourseSerializers
from courses.models import Course
from news.serializers import NewsAdminSerializer
from news.models import News
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

@extend_schema_view(
    create=extend_schema(
        tags=['Admin control'],
        request={
            'multipart/form-data': InstructorSerializer  # ✅ file upload
        }
    ),
    update=extend_schema(
        tags=['Admin control'],
        request={
            'multipart/form-data': InstructorSerializer
        }
    ),
    partial_update=extend_schema(
        tags=['Admin control'],
        request={
            'multipart/form-data': InstructorSerializer
        }
    ),
)

@extend_schema(tags=['Admin control'])
class InstructorAdminControl(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

class CourseAdminControl(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [permissions.IsAdminUser]

class NewsAdminControl(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsAdminSerializer
    permission_classes = [permissions.IsAdminUser]

# class InstructorAdminControl(viewsets.ModelViewSet):
#     queryset = Instructor.objects.all()
#     serializer_class = InstructorSerializer
#     permission_classes = [permissions.IsAdminUser]