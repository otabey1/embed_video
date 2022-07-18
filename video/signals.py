from django.db.models.signals import post_save
from django.dispatch import receiver
from video_encoding import signals
from typing import Type
from video_encoding import tasks
from django_rq import enqueue

from . import tasks as task
from .models import Video

@receiver(post_save, sender=Video)
def convert_video(sender, instance, **kwargs):
    print("convert_video")

    enqueue(tasks.convert_all_videos,
            instance._meta.app_label,
            instance._meta.model_name,
            instance.pk)


@receiver(post_save, sender=Video)
def create_thumbnail(sender, instance, **kwargs):
    print("create_thumbnail")
    enqueue(task.create_thumbnail, instance.pk)


@receiver(signals.encoding_finished, sender=Video)
def mark_as_finished(sender: Type[Video], instance: Video) -> None:
    print("mark_as_finished")
    """
    Mark video as "convertion has been finished".
    """
    
#    video.processed = True
#    video.save(update_fields=['processed'])