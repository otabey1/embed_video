from django.db.models.signals import post_save
from django.dispatch import receiver
from video_encoding import signals
from typing import Type
from video_encoding import tasks
from .models import Video
from kombu import Queue


@receiver(post_save, sender=Video)
def convert_video(sender, instance, **kwargs):
    Queue(tasks.convert_all_videos,
            instance._meta.app_label,
            instance._meta.model_name,
            instance.pk)


@receiver(post_save, sender=Video)
def create_thumbnail(sender, instance, **kwargs):
    Queue(tasks.create_thumbnail, instance.pk)


@receiver(signals.encoding_finished, sender=Video)
def mark_as_finished(sender: Type[Video], instance: Video) -> None:
   """
   Mark video as "convertion has been finished".
   """
   Video.processed = True
   Video.save(update_fields=['processed'])