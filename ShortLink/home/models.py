from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=200)
    shorted_url = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.original_url

    @staticmethod
    def create(original_url,created_date,shorted_url):
        link = ShortenedURL()
        link.original_url = original_url
        link.shorted_url = shorted_url
        link.created_date = created_date
        return link

    @staticmethod
    def get_all(self):
        return list(ShortenedURL.objects.all())

    @staticmethod
    def delete_by_id(link_id):
        """
        :param book_id: an id of a book to be deleted
        :type book_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        if ShortenedURL.get_by_id(link_id) is None:
            return False
        ShortenedURL.objects.get(id=link_id).delete()
        return True