from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=255)
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.title

