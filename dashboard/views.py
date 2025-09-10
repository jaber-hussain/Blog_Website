from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CategoryForm, PostForm, AddUserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def forbidden_message(request, message):
    return render(request, '403.html', {"message": message}, status=403)

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()
    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
@permission_required('blogs.view_category', raise_exception=True)
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login')
@permission_required('blogs.add_category', raise_exception=True)
def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_categories.html', context)

@login_required(login_url='login')
@permission_required('blogs.change_category', raise_exception=True)
def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method=="POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_categories.html', context)

@login_required(login_url='login')
@permission_required('blogs.delete_category', raise_exception=True)
def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


#Functions for posts
@login_required(login_url='login')
@permission_required('blogs.view_blogs', raise_exception=True)
def posts(request):
    posts = Blogs.objects.all()
    context= {
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)

@login_required(login_url='login')
@permission_required('blogs.add_blogs', raise_exception=True)
def add_posts(request):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)

@login_required(login_url='login')
@permission_required('blogs.change_blogs', raise_exception=True)
def edit_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)

    # Restrict Authors: they can only edit their own posts
    if request.user.groups.filter(name='Author').exists() and post.author != request.user:
        return forbidden_message(request, "You are not allowed to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # ✅ Add request.FILES
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'posts': post
    }
    return render(request, 'dashboard/edit_posts.html', context)



@login_required(login_url='login')
@permission_required('blogs.delete_blogs', raise_exception=True)
def delete_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)

    # Restrict Authors: they can only delete their own posts
    if request.user.groups.filter(name='Author').exists() and post.author != request.user:
        return forbidden_message(request, "You are not allowed to delete this post.")

    post.delete()
    return redirect('posts')


#Functions for Users
@login_required(login_url='login')
@permission_required('auth.view_user', raise_exception=True)
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/users.html', context)

@login_required(login_url='login')
@permission_required('auth.add_user', raise_exception=True)
def add_users(request):
    if request.method=='POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = AddUserForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/add_users.html', context)

@login_required(login_url='login')
@permission_required('auth.change_user', raise_exception=True)
def edit_users(request, pk):
    users = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        form = EditUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=users)

    context = {
        'form': form,
        'users': users
    }
    return render(request, 'dashboard/edit_users.html', context)

@login_required(login_url='login')
@permission_required('auth.delete_user', raise_exception=True)
def delete_users(request, pk):
    users = get_object_or_404(User, pk=pk)
    users.delete()
    return redirect('users')