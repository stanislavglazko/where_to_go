# Generated by Django 3.2.9 on 2021-11-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20211105_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Идентификатор'),
        ),
    ]
