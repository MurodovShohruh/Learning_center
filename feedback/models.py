from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from courses.models import Course


class Feedback(models.Model):

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    image = models.URLField(
        max_length=500,
        blank=True,
        null=True
    )

    content = models.TextField()

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="feedbacks"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - ⭐{self.rating}"