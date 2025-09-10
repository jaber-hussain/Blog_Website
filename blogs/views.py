from django.shortcuts import redirect, render, HttpResponse
from blogs.models import Blogs, Category, Comment
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', category__id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts' : posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)

#Blogs
def blogs(request, slug):
   
    blog_post = Blogs.objects.get(status='published', slug=slug)
    
        
    #Comments
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = blog_post
        comment.comment = request.POST['comment']
        comment.save()
        return redirect(f'/blogs/{slug}/#comments')
    
    comments = Comment.objects.filter(blog=blog_post)
    comment_count = comments.count()
    context = {
        'single_post': blog_post,
        'comments': comments,
        'comment_count': comment_count
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
