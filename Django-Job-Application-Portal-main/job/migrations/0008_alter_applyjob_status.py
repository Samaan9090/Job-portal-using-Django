# Generated by Django 3.2.16 on 2024-09-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_applyjob_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Accepted', 'Accepted'), ('Pending', 'Pending')], max_length=20),
        ),
    ]
