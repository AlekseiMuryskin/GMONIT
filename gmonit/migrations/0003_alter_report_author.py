# Generated by Django 4.1.3 on 2022-11-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "gmonit",
            "0002_author_alter_report_camera_alter_report_created_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="gmonit.author",
                verbose_name="Автор",
            ),
        ),
    ]
