# Generated by Django 5.1.1 on 2024-09-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_tabletwo_mb_actually_tabletwo_mb_set_tabletwo_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableone',
            name='diff_reason',
            field=models.CharField(max_length=255, verbose_name='Обоснование отклонения фактического значения'),
        ),
    ]
