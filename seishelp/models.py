from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Create your models here.
class Worker(models.Model):
    POS_CHOICE = (
        ('EN', 'Инженер'),
        ('E1', 'Инженер 1 катогории'),
        ('E2', 'Инженер 2 категории'),
        ('LE', 'Ведущий инженер'),
        ('BS', 'Начальник отдела'),
        ('HR', 'Специалист отдела кадров'),
        ('BH', 'Специалист бухгалтерии')
    )
    name = models.CharField(max_length=255, verbose_name="Ф.И.О.")
    position = models.CharField(max_length=2, choices=POS_CHOICE, verbose_name="Должность")
    email = models.CharField(max_length=255, verbose_name="E-mail")
    telephone = models.CharField(max_length=255, verbose_name="Телефон")

    class Meta:
        ordering = ['name']


class Report(models.Model):
    author = models.ForeignKey(Worker, verbose_name="Автор", on_delete=models.PROTECT)
    mine = models.CharField(max_length=200, verbose_name="Название шахты")
    num_stations=models.IntegerField(verbose_name="Кол-во сработавших станций")
    mag_event=models.FloatField(verbose_name="Магнитуда")
    energy_event=models.FloatField(verbose_name="Энергия")
    xcoo=models.FloatField(verbose_name="X")
    ycoo=models.FloatField(verbose_name="Y")
    zcoo=models.FloatField(verbose_name="Z")
    date_event = models.DateTimeField(default=timezone.now, verbose_name="Дата события")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

