from django.core.management.base import BaseCommand
from myapp3.models import Order



class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        order = Order(name='name3', price=0.3, total_amount=3)
        order.save()
        self.stdout.write(f'{order}')