from django.db import models
from django.urls import reverse


class Course(models.Model):
    """
    A course is a wrapper entity that can contain lectures
    """
    title = models.CharField(max_length=500)
    description = models.TextField()

    syllabus = models.FileField(upload_to="syllabus/", max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"pk": self.pk})
