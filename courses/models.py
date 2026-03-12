from django.db import models
from instructor.models import Instructor

class Course(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "Boshlang'ich"),
        ("middle", "O'rta"),
        ("advanced", "Yuqori"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    students_count = models.IntegerField(default=0)

    rating = models.FloatField(default=0)

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )

    category = models.CharField(max_length=255)

    image = models.URLField()

    skills = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title