# Generated by Django 3.0.5 on 2021-02-22 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210220_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
