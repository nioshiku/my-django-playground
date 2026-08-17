from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='Ass')
    anons = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Article'

