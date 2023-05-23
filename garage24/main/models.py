from django.db import models

class new(models.Model):
    name = models.CharField('Имя', max_length=35)
    number = models.CharField('Номер телефона', max_length=12)
    comment = models.TextField('Комментарий')
    data = models.DateTimeField('Дата записи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'