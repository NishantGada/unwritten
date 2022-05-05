from django.shortcuts import render, get_object_or_404
from .models import Blog_Post, Contact_form_enquirie, Categorie

def index(request):

    cat = Categorie.objects.all()
    latest = Blog_Post.objects.order_by('-timestamp')[0]
    return render(request, 'index.html', {'latest': latest, "cat": cat})

def blogs(request):

    # blog_post = Blog_Post.objects.all()
    blog_post = Blog_Post.objects.order_by('-timestamp')
    return render(request, 'blogs.html', {'blog_post': blog_post})

# def blog1(request, id):

#     post = get_object_or_404(Blog_Post, id=id)
#     return render(request, 'blog1.html', {'post': post})

def blog1(request, title):

    post = get_object_or_404(Blog_Post, title=title)
    return render(request, 'blog1.html', {'post': post})

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact_form_enquirie(name = name, email = email, message = message)
        contact.save()

    return render(request, 'contact.html')


def categories(request, title):

    # category_post = get_object_or_404(Blog_Post, category=title)
    category_post = Blog_Post.objects.filter(category=title)
    return render(request, 'categories.html', {'category_post': category_post})


def search(request):

    query = request.GET['search']

    if len(query) > 50:
        search_posts = Blog_Post.objects.none()
    else:
        search_posts = Blog_Post.objects.filter(title__icontains = query)

    return render(request, 'search.html', {'search_posts': search_posts})


    # search_posts_filter = Blog_Post.objects.filter(title__icontains = query)
    # search_posts_order = Blog_Post.objects.order_by('-timestamp')
    # search_posts =  search_posts_filter.union(search_posts_order)