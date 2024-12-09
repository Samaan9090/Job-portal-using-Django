# Generated by Django 3.2.16 on 2024-09-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_applyjob_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Declined', 'Declined'), ('Accepted', 'Accepted')], max_length=20),
        ),
    ]