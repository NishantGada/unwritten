# Generated by Django 3.0.5 on 2021-02-22 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210222_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_post',
            old_name='date',
            new_name='timestamp',
        ),
    ]
