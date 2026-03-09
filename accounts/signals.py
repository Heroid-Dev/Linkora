from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Profile


@receiver(post_save, sender=Profile)
def assign_group(sender, instance, **kwargs):

    user = instance.user

    if instance.user_type == "COMPANY":
        group, _ = Group.objects.get_or_create(name="employer")
    else:
        group, _ = Group.objects.get_or_create(name="applicant")

    user.groups.clear()
    user.groups.add(group)