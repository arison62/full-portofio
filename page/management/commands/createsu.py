from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config

class Command(BaseCommand):
    help = 'Create a superuser with username "admin" and password "USER_PASSWORD" environment variable'

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = config('USER_PASSWORD')
        if not password:
            self.stdout.write(self.style.ERROR('USER_PASSWORD environment variable is not set.'))
            return
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
            return
        User.objects.create_superuser(username=username, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))