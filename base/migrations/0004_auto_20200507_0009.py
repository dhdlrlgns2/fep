# Generated by Django 2.2.4 on 2020-05-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200506_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='imgur',
            field=models.TextField(editable=False, max_length=100),
        ),
    ]
