from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def populate_contacts_if_empty(sender, **kwargs):
    if sender.name != 'contact':
        return

    from contact.models import Contact

    if Contact.objects.exists():
        return

    call_command('populate_contacts')
