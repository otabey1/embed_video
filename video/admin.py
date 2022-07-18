from django.contrib import admin
from video_encoding.admin import FormatInline

from .models import Video



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = (FormatInline, )

    list_display = ('title', )

    fields = ('title', 'width',  'height', 'duration', 'file',)

    readonly_fields = ('width', 'height', 'duration')
