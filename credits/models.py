from django.conf import settings

# for Django 1.5 support
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

from django.db import models


class Profile(models.Model):
    """
    For testing, track the number of "credits".
    """
    user = models.ForeignKey(AUTH_USER_MODEL)
    credits = models.PositiveIntegerField(default=0)


def user_post_save(sender, instance, created, raw, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
models.signals.post_save.connect(user_post_save, sender=User)
