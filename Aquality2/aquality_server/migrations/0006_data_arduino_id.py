# Generated by Django 3.1.3 on 2021-01-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquality_server', '0005_auto_20210118_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='arduino_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]