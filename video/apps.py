from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'

# from django.apps import AppConfig


# class MyAppConfig(AppConfig):
#    # ...

#     def ready(self) -> None:
#       from . import signals  # register signals
