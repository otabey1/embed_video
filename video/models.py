from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _
from video_encoding.fields import VideoField
from video_encoding.models import Format



class Video(models.Model):
    title = models.CharField(_('Test'), max_length=100)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)

    file = VideoField(_("Video file"), width_field='width', height_field='height', duration_field='duration', upload_to='movie/%Y/%m/%d')

    format_set = GenericRelation(Format)

    class Meta:
        verbose_name = _('Kino')
        verbose_name_plural = _('Kinolar')

    def __str__(self):
        return self.title
