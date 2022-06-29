from django.core.files import File
import os
from video_encoding.backends import get_backend
from video.models import Video


def create_thumbnail(video_pk):
   video = Video.objects.get(pk=video_pk)
   if not video.file:
      # no video file attached
      return

   if video.thumbnail:
      # thumbnail has already been generated
      return

   encoding_backend = get_backend()
   thumbnail_path = encoding_backend.get_thumbnail(video.file.path)
   filename = os.path.basename(self.url),

   try:
      with open(thumbnail_path, 'rb') as file_handler:
         django_file = File(file_handler)
         video.thumbnail.save(filename, django_file)
      video.save()
   finally:
      os.unlink(thumbnail_path)