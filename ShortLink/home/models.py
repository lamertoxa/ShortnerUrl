from django.db import models
import string
import secrets
class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=200)
    shorted_url = models.URLField(max_length=200,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs):
        if not self.shorted_url:
            self.shorted_url = self.generate_random_string()
            while ShortenedURL.objects.filter(shorted_url=self.shorted_url).exists():
                self.shorted_url = self.generate_random_string()
        super().save(*args, **kwargs)
    @staticmethod
    def generate_random_string(length=8):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(secrets.choice(characters) for _ in range(length))
        return random_string

    @staticmethod
    def create(original_url):

        link = ShortenedURL()
        link.original_url = original_url
        link.shorted_url =ShortenedURL.generate_random_string()
        link.save()
        return link

    @staticmethod
    def get_all(self):
        return list(ShortenedURL.objects.all())

    @staticmethod
    def delete_by_id(link_id):

        if ShortenedURL.get_by_id(link_id) is None:
            return False
        ShortenedURL.objects.get(id=link_id).delete()
        return True