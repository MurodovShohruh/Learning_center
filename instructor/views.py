from rest_framework import generics, permissions
from .models import Instructor
from .serializers import InstructorSerializers
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Ustozlar royxati'])
class InstructorListView(generics.ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers

class InstructorDetailView(generics.RetrieveAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers

class InstructorCreateView(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers
    permission_classes = [permissions.IsAdminUser]

class InstructorUpdateView(generics.UpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers
    permission_classes = [permissions.IsAdminUser]

class InstructorDeleteView(generics.DestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers
    permission_classes = [permissions.IsAdminUser]
