from django.apps import AppConfig
from django.db.models.signals import post_migrate

def clear_stories(sender, **kwargs):
    from .models import Story
    Story.objects.all().delete()

class StoriesConfig(AppConfig):
    name = 'stories'

    def ready(self):
        post_migrate.connect(clear_stories, sender=self)
