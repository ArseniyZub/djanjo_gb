from django.core.management.base import BaseCommand
from myapp4.models import Order, Client


class Command(BaseCommand):
    help = "Creating orders for clients"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            for i in range(1, 2):
                order = Order(client=client, total_amount=i * 3) 
                order.save()
                self.stdout.write(f'Order for {client.name} created')