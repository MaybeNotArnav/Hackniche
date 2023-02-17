from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SiteUser
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        print(instance)
        SiteUser.objects.create(user=instance)

