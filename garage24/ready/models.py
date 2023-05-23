from django.db import models

class Ready(models.Model):
    brand = models.CharField('Марка машины', max_length=35)
    comment = models.TextField('Комментарий')
    photo = models.ImageField(upload_to='media/' 'Фотография авто', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Наши работы'