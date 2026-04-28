<div align="center">

# Django Blog Platform ✍️

**A Full-Featured Blog Web App - Built with Django**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/licenses/MIT)

> A clean, functional blog platform with a public-facing site and a full admin dashboard for managing posts, categories, users, and comments.

</div>

---

## 📌 What is this?

A Django-based blog platform with two distinct layers - a **public blog site** for readers and a **dashboard** for authors and admins to manage content. Built with server-side rendering using Django templates.

---

## ✨ Features

### 🌐 Public Site
- Home page with latest blog posts
- Browse posts by category
- Full blog post detail page with comments
- Search functionality across posts
- Custom 403, 404, and 500 error pages

### 🖥️ Admin Dashboard
- Post management - add, edit, delete posts
- Category management - add, edit, delete categories
- User management - add, edit, manage users
- Comment management
- Rich text post creation with image upload support
- Post status control (draft / published)
- Left sidebar navigation

### 🔐 Auth
- User registration and login
- Role-based access with decorators

---

## 🏗️ Project Structure

```
├── blogs/             # Core blog app - posts, categories, comments,
│                      # context processors, views
├── dashboard/         # Admin dashboard - post, category, user management
│                      # forms, views, templates
├── blog_main/         # Project config - settings, urls, forms, views
└── templates/
    ├── base/          # Base layout, header, footer
    ├── dashboard/     # Dashboard pages (posts, categories, users)
    ├── blogs.html     # Blog listing page
    ├── home.html      # Home page
    ├── search.html    # Search results
    ├── login.html     # Login page
    ├── register.html  # Registration page
    └── 403/404/500    # Custom error pages
```

---

## 🔌 Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 4.x |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | Django Templates + Custom CSS |
| Media | Image uploads with date-based folder structure |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/jaber-hussain/django-blog.git
cd django-blog

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirement.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

## 👨‍💻 Author

**Jaber Hussain**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jaber-hussain/)
[![Fiverr](https://img.shields.io/badge/Fiverr-1DBF73?style=flat-square&logo=fiverr&logoColor=white)](https://www.fiverr.com/jaberhussain503)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jaberchaudary@gmail.com)

---

<div align="center">

*Built with ❤️ using Django*

</div>
