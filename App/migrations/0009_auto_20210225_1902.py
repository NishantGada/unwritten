# Generated by Django 3.0.5 on 2021-02-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20210222_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='description',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='categorie',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='media/category_thumbnails'),
        ),
    ]
