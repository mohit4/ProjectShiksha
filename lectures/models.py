from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Lecture(models.Model):
    """
    A lecture is an entity that contains study material
    """
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    published_date = models.DateTimeField(auto_now_add=True)

    video_link = models.URLField(max_length=500, null=True, blank=True)
    content_files = models.FileField(upload_to="lectures/uploads/", max_length=500, null=True, blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lectures')

    def __str__(self):
        return f"{self.title} by {self.creator.first_name} {self.creator.last_name}"
    
    def get_absolute_url(self):
        return reverse("lectures:lecture-detail", kwargs={"pk": self.pk})
