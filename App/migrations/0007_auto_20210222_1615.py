# Generated by Django 3.0.5 on 2021-02-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20210222_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='category',
            field=models.CharField(choices=[('Programming', 'Programming'), ('Food', 'Food'), ('Fitness', 'Fitness'), ('Health', 'Health')], default='', max_length=100),
        ),
    ]
