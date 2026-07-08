import random

from django.core.management.base import BaseCommand
from faker import Faker

from contact.models import Category, Contact

CATEGORIES = ['Trabalho', 'Amigos', 'Família', 'Serviços']


class Command(BaseCommand):
    help = 'Cria contatos aleatórios a cada execução.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=20,
            help='Quantidade de contatos a criar (padrão: 20).',
        )

    def handle(self, *args, **options):
        fake = Faker('pt_BR')
        count = options['count']

        categories = [
            Category.objects.get_or_create(name=name)[0]
            for name in CATEGORIES
        ]

        contacts = []
        for _ in range(count):
            contacts.append(
                Contact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    email=fake.unique.email(),
                    description=fake.sentence(nb_words=8),
                    category=random.choice(categories),
                    show=True,
                )
            )

        Contact.objects.bulk_create(contacts)

        self.stdout.write(
            self.style.SUCCESS(
                f'{count} contato(s) aleatório(s) criado(s). '
                f'Total no banco: {Contact.objects.count()}.'
            )
        )
