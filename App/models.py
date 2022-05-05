from django.db import models
import datetime
from ckeditor.fields import RichTextField


# categories = [
#     ('Programming', 'Programming'),
#     ('Food', 'Food'),
#     ('Fitness', 'Fitness'),
#     ('Health', 'Health'),
# ]


class Categorie(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120, default="")
    thumbnail = models.ImageField(upload_to="media/category_thumbnails", default="")

    def __str__(self):
        return self.title


class Blog_Post(models.Model):
    title = models.CharField(max_length=300, default="")
    # category = models.CharField(max_length=100, choices=categories, default="")
    category = models.ManyToManyField(Categorie)
    description = models.CharField(max_length=200, default="")
    body = RichTextField(blank=False, null=False, default="")
    # body = models.TextField(max_length=3000, default="")
    cover_image = models.ImageField(upload_to='media/cover_images')
    author = models.CharField(max_length=300, default="Nishant Gada")
    timestamp = models.DateTimeField(auto_now_add=True, null=False)


class Contact_form_enquirie(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    email = models.EmailField(max_length=500, blank=False, null=False)
    message = models.TextField(max_length=1000, default="", blank=False, null=False)
    
