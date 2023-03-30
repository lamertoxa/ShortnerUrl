from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from ShortLink.home.models import ShortenedURL

class Command(BaseCommand):
    help = 'Deletes shortened links that are older than 90 days.'

    def handle(self, *args, **options):
        expiration_date = timezone.now() - timedelta(days=90)
        old_links = ShortenedURL.objects.filter(created_at__lte=expiration_date)
        old_links_count = old_links.count()
        old_links.delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {old_links_count} old links.'))