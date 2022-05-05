from django.contrib import admin
from App.models import Blog_Post, Contact_form_enquirie, Categorie

class Contact(admin.ModelAdmin):
    list_display = ("name", "email")


class Post(admin.ModelAdmin):
    list_display = ("title", "timestamp")

admin.site.register(Blog_Post, Post)
admin.site.register(Contact_form_enquirie, Contact)
admin.site.register(Categorie)



# from django.contrib import admin
# from App.models import Blog_Post, Contact_form_enquirie, Categorie

# class Contact(admin.ModelAdmin):
#     list_display = ("name", "email")

# @admin.register(Blog_Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("title", "timestamp")

#     class Media:
#         js = ('static/tinyMCE.js')

# # admin.site.register(Post)
# admin.site.register(Contact_form_enquirie, Contact)
# admin.site.register(Categorie)