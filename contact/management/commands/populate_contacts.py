from django.core.management.base import BaseCommand

from contact.models import Category, Contact


CONTACTS = [
    {
        'first_name': 'Ana',
        'last_name': 'Silva',
        'phone': '11987654321',
        'email': 'ana.silva@email.com',
        'description': 'Colega de trabalho do setor financeiro.',
        'category': 'Trabalho',
    },
    {
        'first_name': 'Bruno',
        'last_name': 'Oliveira',
        'phone': '21976543210',
        'email': 'bruno.oliveira@email.com',
        'description': 'Amigo da faculdade.',
        'category': 'Amigos',
    },
    {
        'first_name': 'Carla',
        'last_name': 'Santos',
        'phone': '31965432109',
        'email': 'carla.santos@email.com',
        'description': 'Prima que mora em Belo Horizonte.',
        'category': 'Família',
    },
    {
        'first_name': 'Daniel',
        'last_name': 'Ferreira',
        'phone': '41954321098',
        'email': 'daniel.ferreira@email.com',
        'description': 'Eletricista de confiança.',
        'category': 'Serviços',
    },
    {
        'first_name': 'Elena',
        'last_name': 'Costa',
        'phone': '51943210987',
        'email': 'elena.costa@email.com',
        'description': 'Gerente de projetos.',
        'category': 'Trabalho',
    },
    {
        'first_name': 'Felipe',
        'last_name': 'Almeida',
        'phone': '61932109876',
        'email': 'felipe.almeida@email.com',
        'description': 'Vizinho do apartamento 302.',
        'category': 'Amigos',
    },
    {
        'first_name': 'Gabriela',
        'last_name': 'Rocha',
        'phone': '71921098765',
        'email': 'gabriela.rocha@email.com',
        'description': 'Irmã mais nova.',
        'category': 'Família',
    },
    {
        'first_name': 'Henrique',
        'last_name': 'Mendes',
        'phone': '81910987654',
        'email': 'henrique.mendes@email.com',
        'description': 'Personal trainer.',
        'category': 'Serviços',
    },
    {
        'first_name': 'Isabela',
        'last_name': 'Lima',
        'phone': '85909876543',
        'email': 'isabela.lima@email.com',
        'description': 'Designer da equipe de marketing.',
        'category': 'Trabalho',
    },
    {
        'first_name': 'João',
        'last_name': 'Pereira',
        'phone': '85998765432',
        'email': 'joao.pereira@email.com',
        'description': 'Amigo do futebol de domingo.',
        'category': 'Amigos',
    },
    {
        'first_name': 'Karina',
        'last_name': 'Martins',
        'phone': '85987654321',
        'email': 'karina.martins@email.com',
        'description': 'Tia que organiza os encontros da família.',
        'category': 'Família',
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Barbosa',
        'phone': '85976543210',
        'email': 'lucas.barbosa@email.com',
        'description': 'Mecânico da oficina perto de casa.',
        'category': 'Serviços',
    },
    {
        'first_name': 'Mariana',
        'last_name': 'Gomes',
        'phone': '85965432109',
        'email': 'mariana.gomes@email.com',
        'description': 'Recursos humanos.',
        'category': 'Trabalho',
    },
    {
        'first_name': 'Nicolas',
        'last_name': 'Ribeiro',
        'phone': '85954321098',
        'email': 'nicolas.ribeiro@email.com',
        'description': 'Colega do grupo de estudos.',
        'category': 'Amigos',
    },
    {
        'first_name': 'Olivia',
        'last_name': 'Carvalho',
        'phone': '85943210987',
        'email': 'olivia.carvalho@email.com',
        'description': 'Avó materna.',
        'category': 'Família',
    },
    {
        'first_name': 'Paulo',
        'last_name': 'Araújo',
        'phone': '85932109876',
        'email': 'paulo.araujo@email.com',
        'description': 'Encanador indicado pelo prédio.',
        'category': 'Serviços',
    },
    {
        'first_name': 'Rafaela',
        'last_name': 'Nunes',
        'phone': '85921098765',
        'email': 'rafaela.nunes@email.com',
        'description': 'Analista de suporte.',
        'category': 'Trabalho',
    },
    {
        'first_name': 'Samuel',
        'last_name': 'Dias',
        'phone': '85910987654',
        'email': 'samuel.dias@email.com',
        'description': 'Amigo de viagens.',
        'category': 'Amigos',
    },
    {
        'first_name': 'Tatiana',
        'last_name': 'Monteiro',
        'phone': '85909876540',
        'email': 'tatiana.monteiro@email.com',
        'description': 'Prima que trabalha como médica.',
        'category': 'Família',
    },
    {
        'first_name': 'Vinícius',
        'last_name': 'Teixeira',
        'phone': '85998765012',
        'email': 'vinicius.teixeira@email.com',
        'description': 'Dentista da família.',
        'category': 'Serviços',
    },
]


class Command(BaseCommand):
    help = 'Popula o banco com 20 contatos de exemplo.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Remove todos os contatos antes de popular.',
        )

    def handle(self, *args, **options):
        if options['clear']:
            deleted, _ = Contact.objects.all().delete()
            self.stdout.write(self.style.WARNING(f'{deleted} contato(s) removido(s).'))

        categories = {}
        for contact_data in CONTACTS:
            category_name = contact_data['category']
            if category_name not in categories:
                category, _ = Category.objects.get_or_create(name=category_name)
                categories[category_name] = category

        created_count = 0
        for contact_data in CONTACTS:
            category = categories[contact_data['category']]
            _, created = Contact.objects.get_or_create(
                email=contact_data['email'],
                defaults={
                    'first_name': contact_data['first_name'],
                    'last_name': contact_data['last_name'],
                    'phone': contact_data['phone'],
                    'description': contact_data['description'],
                    'category': category,
                    'show': True,
                },
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'{created_count} contato(s) criado(s). '
                f'Total no banco: {Contact.objects.count()}.'
            )
        )
