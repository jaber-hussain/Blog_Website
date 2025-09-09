from django.shortcuts import redirect, render, HttpResponse
from blogs.models import Blogs, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', category__id=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return render(request, '404.html', status=404)
    context = {
        'posts' : posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)

#Blogs
def blogs(request, slug):
    try:
        blog_post = Blogs.objects.get(status='published', slug=slug)
    except Blogs.DoesNotExist:
        return render(request, '404.html', status=404)

    context = {
        'single_post': blog_post
    }
    return render(request, 'blogs.html', context)

#Search
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='published')
    content = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', content)
