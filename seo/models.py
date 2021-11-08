from django.db import models

# Create your models here.
class LatestNews(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title