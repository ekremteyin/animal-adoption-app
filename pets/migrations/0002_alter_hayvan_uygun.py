# Generated by Django 5.0.6 on 2024-05-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hayvan',
            name='uygun',
            field=models.BooleanField(default=False, verbose_name='Uygun'),
        ),
    ]
