from django.conf import settings
from django.db import models

class Story(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authored_stories')
    text = models.TextField()
    partner_story = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appeal_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Story by {self.author}"
