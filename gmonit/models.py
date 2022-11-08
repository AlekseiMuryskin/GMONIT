from django.db import models
from django.utils import timezone

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
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Mine(models.Model):
    name=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Camera(models.Model):
    name=models.CharField(max_length=255)
    mine=models.ForeignKey(Mine,on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Report(models.Model):
    author = models.ForeignKey(Worker, verbose_name="Автор", on_delete=models.PROTECT)
    title = models.CharField(max_length=200, verbose_name="Название отчета")
    mine = models.ForeignKey(Mine,max_length=200, verbose_name="Название шахты", on_delete=models.PROTECT)
    camera = models.ForeignKey(Camera,max_length=200, verbose_name="Название камеры", on_delete=models.PROTECT)
    text = models.TextField(verbose_name="Текст отчета")
    num_destroy_blocks = models.IntegerField(verbose_name="Кол-во частично разрушенных целиков")
    num_crack_blocks = models.IntegerField(verbose_name="Кол-во полностью разрушенных целиков")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата")
    def __str__(self):
        return self.title
