# Generated by Django 3.2.16 on 2024-09-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='est_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
