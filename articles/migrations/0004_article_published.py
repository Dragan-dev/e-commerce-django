# Generated by Django 3.2.7 on 2022-07-08 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20220707_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
