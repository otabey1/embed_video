from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    title = models.CharField(max_length=500)
    video = EmbedVideoField()