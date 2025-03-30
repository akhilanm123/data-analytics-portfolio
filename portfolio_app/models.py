from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Prevent duplicate titles
    description = models.TextField()
    skills = models.CharField(max_length=300, blank=True)  # New: Technologies used
    github_link = models.URLField(blank=True, null=True)  # New: GitHub repo
    live_demo = models.URLField(blank=True, null=True)  # New: Live project link
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # Existing: Project image

    def __str__(self):
        return self.title


from django.db import models

from django.db import models


class Skill(models.Model):  # ✅ Correctly formatted class
    name = models.CharField(max_length=200)  # Skill name (e.g., "SQL, Python, etc.")

    def __str__(self):
        return self.name  # ✅ Makes skills readable in the admin panel
