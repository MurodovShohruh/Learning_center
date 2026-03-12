from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorAdminControl, CourseAdminControl, NewsAdminControl

router = DefaultRouter()
router.register('instructor/admin', InstructorAdminControl, basename='instructor-admin')
router.register('course/admin', CourseAdminControl, basename='course-admin')
router.register('news/admin', NewsAdminControl, basename='news-admin')

urlpatterns = [
    path('', include(router.urls)),
]