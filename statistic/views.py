from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser
from courses.models import Course
from instructor.models import Instructor

class ShowStatistic(APIView):
    def get(self, request):
        teachers = Instructor.objects.count()
        courses = Course.objects.count()
        users = CustomUser.objects.count()

        data = {
            "Users": users,
            "teachers_count": teachers,
            "courses_count": courses
        }


        return Response(data, status=status.HTTP_200_OK)