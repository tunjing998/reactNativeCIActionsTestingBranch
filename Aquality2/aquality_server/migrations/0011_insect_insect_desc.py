# Generated by Django 3.1.3 on 2021-01-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquality_server', '0010_insect'),
    ]

    operations = [
        migrations.AddField(
            model_name='insect',
            name='insect_desc',
            field=models.TextField(null=True),
        ),
    ]
