# Generated by Django 4.1.3 on 2022-11-07 13:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Ф.И.О.")),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("EN", "Инженер"),
                            ("E1", "Инженер 1 катогории"),
                            ("E2", "Инженер 2 категории"),
                            ("LE", "Ведущий инженер"),
                            ("BS", "Начальник отдела"),
                            ("HR", "Специалист отдела кадров"),
                            ("BH", "Специалист бухгалтерии"),
                        ],
                        max_length=2,
                        verbose_name="Должность",
                    ),
                ),
                ("email", models.CharField(max_length=255, verbose_name="E-mail")),
                ("telephone", models.CharField(max_length=255, verbose_name="Телефон")),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mine",
                    models.CharField(max_length=200, verbose_name="Название шахты"),
                ),
                (
                    "num_stations",
                    models.IntegerField(verbose_name="Кол-во сработавших станций"),
                ),
                ("mag_event", models.FloatField(verbose_name="Магнитуда")),
                ("energy_event", models.FloatField(verbose_name="Энергия")),
                ("xcoo", models.FloatField(verbose_name="X")),
                ("ycoo", models.FloatField(verbose_name="Y")),
                ("zcoo", models.FloatField(verbose_name="Z")),
                (
                    "date_event",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Дата события"
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Дата"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="seishelp.worker",
                        verbose_name="Автор",
                    ),
                ),
            ],
        ),
    ]
