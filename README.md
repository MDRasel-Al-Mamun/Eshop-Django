# Eshop-Ecommerce

To Create a E-Commerce Website with Django

> - <a href="#templates">1. Templates Setup </a>

> - <a href="#product">2. Product Model Setup </a>

> - <a href="#image">3. Image Model Setup </a>

> - <a href="#tinymceeditor">4. TinyMCE Editor Setup </a>

> - <a href="#Setting">5. Setting Model & About / Contact Page </a>

> - <a href="#contact">6. Contact Form Submit </a>

> - <a href="#subcategory">7. Sub Category Setup </a>

> - <a href="#slug">8. Auto Slug Create </a>

> - <a href="#slider">9. Slider Daynamic </a>

> - <a href="#image_dy">10. Images Daynamic </a>

> - <a href="#ca-products">11. Category Products Show </a>

> - <a href="#search">12. Search Products </a>

> - <a href="#autosearch">13. Auto Search Ajax </a>

> - <a href="#single">14. Single Page Dynamic </a>

> - <a href="#comments">15. Single Page Comments </a>

> - <a href="#cart">16. Add & Delete Cart </a>

> - <a href="#login">17. User Model & Login </a>

> - <a href="#signup">18. Sign Up Form </a>

> - <a href="#myaccount">19. User Account Page </a>

> - <a href="#update">20. Update User Profile </a>

> - <a href="#password">21. User Password Change </a>

> - <a href="#ordercomplete">22. Order Form & Complete It </a>

> - <a href="#orderdetail">23. User Order & Order Details </a>

> - <a href="#comment-delete">24. User Comment & Delete </a>

> - <a href="#avg-count">25. Product Review Avg & Count </a>

> - <a href="#faq">26. Frequently Asked Questions </a>

> - <a href="#variant">27. Variant Product Setup  </a>

> - <a href="#tags">28. Custom Templates Tags  </a>


# 1. Django Setup & Templates <a href="" name="templates"> - </a>

### Command Prompt -

- > virtualenv env
- > pip install django
- > pip install pillow
- > pip install pylint
- > pip install autopep8
- > django-admin startproject ecommerce .
- > python manage.py startapp home
- > python manage.py migrate
- > python manage.py createsuperuser

    - > username - \***\*\*\*\*\***
    - > email - \***\*\*\*\*\***
    - > password - \***\*\*\*\*\***
    - > re-password - \***\*\*\*\*\***

- > python manage.py runserver

### ecommerce > settings.py -

```python
INSTALLED_APPS = [
    'home.apps.HomeConfig',
]

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```

### ecommerce > urls.py -

```python
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### home > create file & folder -

- > urls.py
>
- >templates -
    - > base.html
    - > index.html
    - > css.html
    - > header.html
    - > footer.html
    - > scripts.html
    - > content.html
    - > sidebar.html
    - > slider.html
    - > message.html
>
- > static
    - > css ---- All stylesheet Files
    - > fonts ---- Website Fonts
    - > img ---- All Static Image
    - > js ---- All Javascript File

### home > views.py -

```python
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)
```

### home > urls.py -

```python
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home')
]
```

### ecommerce > urls.py -

```python
from home import views as home

urlpatterns = [

    # Home App Urls
    path('', home.index, name='home'),
]
```


### home > templates > base.html -

```django
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{% block title %} Home {% endblock %}</title>
    <meta name="keywords" content="{% block keywords %} Keywords {% endblock %}">
    <meta name="description" content="{% block description %} Description {% endblock %}">

    {% include 'css.html' %}

    {% block stylesheet %}

    {% endblock %}

</head>

<body>
    {% include 'header.html' %}

    {% block message %} {% endblock %}

    {% block sidebar %} {% endblock %}

    {% block slider %} {% endblock %}


    {% block content %}

    {% endblock %}


    {% include 'footer.html' %}

    {% include 'scripts.html' %}

    {% block scripts %}

    {% endblock %}

</body>

</html>
```

### home > templates > index.html -

```django
{% extends 'base.html' %}

{% load static %}

{% block title %} {% endblock %}

{% block keywords %} {% endblock %}

{% block description %} {% endblock %}

{% block stylesheet %} {% endblock %}

{% block message %} {% include 'message.html' %} {% endblock %}

{% block sidebar %} {% include 'sidebar.html' %} {% endblock %}

{% block slider %} {% include 'slider.html' %} {% endblock %}


{% block content %} {% include 'content.html' %} {% endblock %}


{% block scripts %} {% endblock %}

```

### home > templates > message.html -

```python
{% load static %}

{% if messages %}
{% for message in messages %}
<div class="alert alert-{{message.tags}}" role="alert">
    <div class="container">
        {{ message }}
    </div>
</div>
{% endfor %}
{% endif %}
```

### HTML Code( Show Templates ) -

```html
<img src="{% static './img/*****.jpg' %}" alt="*****">

<link rel="stylesheet" href="{% static 'css/*****.css' %}">

<script src="{% static 'js/*****.js' %}"></script>
```

### Command Prompt -

- > python manage.py runserver


# 2. Product Model <a href="" name="product"> - </a>

### Command Prompt -

- > python manage.py startapp product

### ecommerce > settings.py -

```python
INSTALLED_APPS = [
    'product.apps.ProductConfig',
]
```

### ecommerce > urls.py -

```python
urlpatterns = [
    path('product/', include('product.urls')),
]
```

### product > create file & folder -

- > urls.py
- > templates

### product > models.py -

```python
from django.db import models

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/category/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/product/', null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    minamount = models.IntegerField()
    detail = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

### product > admin.py -

```python
from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'parent', 'status']
    search_fields = ['__str__', 'title']
    list_per_page = 10

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'category', 'status']
    search_fields = ['__str__', 'title', 'price']
    list_filter = ['category']
    list_per_page = 10

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > python manage.py runserver
- > [ Create Some Category & Product ]

# 3. Image Model Setup <a href="" name="image"> - </a>

### product > models.py -

```python
from django.utils.safestring import mark_safe

class Product(models.Model):

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
```

### product > admin.py -

```python
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'category', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    list_per_page = 10


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    list_per_page = 10

    class Meta:
        model = Images


admin.site.register(Images, ImagesAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > python manage.py runserver
- > [ Upload Some Images ]

# 4. TinyMCE Editor Setup <a href="" name="tinymceeditor"> - </a>

### Command Prompt -

- > pip install django-tinymce

### ecommerce > settings.py -

```python
INSTALLED_APPS = [
    'tinymce',
]

TINYMCE_JS_URL = os.path.join(STATIC_URL, "js/tinymce/tinymce.min.js")

TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "js/tinymce")

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'image_caption': True,
    'image_advtab': True,
    'plugins': '''
            textcolor save link image imagetools media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'file_browser_callback': "myFileBrowser",
}
```

### home > static > js -

> ##### Copy [ Components > tinymce_latest_custom.zip ] All tinymce Folder & Files
> ##### Paste All Those [ home > static > js > tinymce ] In Here


### ecommerce > urls.py -

```python
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
]
```

### product > models.py -

```python
from tinymce.models import HTMLField

class Product(models.Model):
    details = HTMLField()
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > python manage.py runserver
- > [ Use TinyMCE Editor For Post]

# 5. Setting Model & About / Contact Page <a href="" name="setting"> - </a>

### home > templates > create file -

- > about.html
- > contact.html

### home > models.py -

```python
from django.db import models
from tinymce.models import HTMLField

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True,max_length=200)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=50)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=200)
    instagram = models.CharField(blank=True,max_length=200)
    twitter = models.CharField(blank=True,max_length=200)
    youtube = models.CharField(blank=True, max_length=200)
    aboutus = HTMLField(blank=True)
    contact = HTMLField(blank=True)
    references = HTMLField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

### home > admin.py -

```python
from django.contrib import admin
from .models import *


class SettingtAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'company', 'update_at', 'status']
    search_fields = ['__str__', 'company']
    list_filter = ['company']
    list_per_page = 10

    class Meta:
        model = Setting


admin.site.register(Setting, SettingtAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > python manage.py runserver
- > [ Completa All the fields on Setting Models - 127.0.0.1:8000/admin ]

### home > views.py -

```python
from django.shortcuts import render
from .models import Setting

def index(request):
    setting = Setting.objects.get(pk=1)
    page = "home"
    context = {
        'setting': setting,
        'page':page,
    }
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, 'contact.html', context)
```

### ecommerce > urls.py -

```python
from home import views as home

urlpatterns = [
    path('about/', home.about, name='about'),
    path('contact/', home.contact, name='contact'),
]
```

### home > templates > index.html -

```python
{% block title %} {{ setting.title }} {% endblock %}

{% block keywords %} {{ setting.keywords }} {% endblock %}

{% block description %} {{ setting.description }} {% endblock %}
```

### home > templates > sidebar.html -

```html
<!-- category nav -->
{% if page %}
    <div class="category-nav">
{% else %}
    <div class="category-nav show-on-click">
{% endif %}
```

### home > templates > about.html -

```html
<div class="row">
    {{ setting.aboutus|safe }}
</div>
```

### home > templates > contact.html -

```html
<div class="row">
    <div class="col-lg-6 col-md-6">
        <div class="section-title">
			<h3 class="title">Contact Form</h3>
		</div>
        <form id="checkout-form" class="clearfix" method="POST" action="" enctype="multipart/form-data">
			<div class="form-group">
				<input class="input" type="text" name="first-name" placeholder="Name">
			</div>
			<div class="form-group">
				<input class="input" type="text" name="last-name" placeholder="Subject">
			</div>
			<div class="form-group">
				<input class="input" type="email" name="email" placeholder="Email">
            </div>
            <div class="form-group">
                <textarea name="massage"  cols="30" rows="10">Massage</textarea>	
            </div>		
		    <input class="btn btn-info" type="submit" value="Send Message">
		</form>
    </div>
    <div class="col-lg-6 col-md-6">
        <div class="section-title">
			<h3 class="title">Contact Information</h3>
		</div>
        {{ setting.contact|safe }}
    </div>
</div>
```

# 6. Contact Form Submit <a href="" name="contact"> - </a>

### home > models.py -

```python
from django.forms import ModelForm, TextInput, Textarea

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'placeholder': 'Subject'}),
            'email': TextInput(attrs={'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'placeholder': 'Your Message'}),
        }
```

### home > admin.py -

```python
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'update_at', 'status']
    readonly_fields = ('__str__', 'subject', 'email', 'message', 'ip')
    search_fields = ['__str__', 'subject']
    list_filter = ['status']
    list_per_page = 10

    class Meta:
        model = ContactMessage

admin.site.register(ContactMessage, ContactMessageAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > pip install django-crispy-forms

### ecommerce > settinds.py -

```python
INSTALLED_APPS = [
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'
```

### home > views.py -

```python
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from .models import ContactForm, ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')
    form = ContactForm
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
        'form': form,
    }
    return render(request, 'contact.html', context)
```

### home > templates > contact.html -

```html
{% load crispy_forms_tags %}

<div class="section-title">
    <h3 class="title">Contact Form</h3>
</div>

{{ form.media }}
<form id="checkout-form" class="clearfix" method="POST" action="" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <input class="btn btn-info" type="submit" value="Send Message">
</form>
```

# 7. Sub Category Setup <a href="" name="subcategory"> - </a>

### Command Prompt -

- > pip install django-mptt

### ecommerce > settings.py -

```python
INSTALLED_APPS = [
    'mptt',
]
```

### product > models.py -

```python
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Category(MPTTModel):

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
```

### product > admin.py -

```python
from mptt.admin import DraggableMPTTAdmin

class CategoryAdminMptt(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    search_fields = ['__str__', 'title']
    list_per_page = 10

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(qs, Product, 'category', 'products_cumulative_count', cumulative=True)

        qs = Category.objects.add_related_count(qs, Product, 'category', 'products_count', cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

admin.site.register(Category, CategoryAdminMptt)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > [ Delete All Category & Create New Category & Sub Category and Link to the Peoducts ]

### home > views.py -

```python
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from product.models import Category, Product, Images

def index(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'index.html', context)

def about(request):
    category = Category.objects.all()

    context = {
        'category': category,
    }
    return render(request, 'about.html', context)


def contact(request):
    category = Category.objects.all()

    context = {
        'category': category,
    }
    return render(request, 'contact.html', context)
```


### home > templates > sidebar.html -

```html
{% load mptt_tags %}

{% if page %}
<div class="category-nav">
    {% else %}
    <div class="category-nav show-on-click">
        {% endif %}
        <span class="category-header">Categories <i class="fa fa-list"></i></span>
        <ul class="category-list">
            {% recursetree category %}
            <li class="dropdown side-dropdown">
                <a href="" class="dropdown-toggle" {% if not node.is_leaf_node %} data-toggle="dropdown" aria-expanded="true"{% endif %}>{{ node.title }}  <i class="fa fa-angle-right"></i></a>
                <div class="custom-menu">
                    <div class="row">
                        <div class="col-md-4">
                        {% if not node.is_leaf_node %}
                            <ul class="list-links">
                                <li><a href="#">{{ children }}</a></li>
                            </ul>
                        {% endif %}
                        <hr class="hidden-md hidden-lg">
                        </div>
                    </div>
                </div>
            </li>
            {% endrecursetree %}
        </ul>
    </div>
</div>
```

# 8. Auto Slug Create <a href="" name="slug"> - </a>

### product > models.py -

```python
from django.urls import reverse

class Category(MPTTModel):

    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(MPTTModel):

    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
```

### product > admin.py -

```python
class CategoryAdminMptt(DraggableMPTTAdmin):

    prepopulated_fields = {'slug': ('title',)}

class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
```

# 9. Slider Dynamic <a href="" name="slider"> - </a>

### home > views.py -

```python
def index(request):
    product_slider = Product.objects.all()
    product_slider = Product.objects.filter(featured=True)[:3]
    context = {
        'product_slider': product_slider,
    }
    return render(request, 'index.html', context)
```

### home > templates > slider.html -

```html
{% for slider in product_slider %}
<div class="banner banner-1">
    <img src="{{ slider.image.url }}" height="560px" alt="">
    <div class="banner-caption text-center">
        <h1 style="color: #F8694A;">{{ slider.title|truncatewords:"4" }}</h1>
        <h3 class="white-color font-weak">$ {{ slider.price }}</h3>
        <a href="/product/{{ slider.id }}/{{ slider.slug }}" class="primary-btn">Shop Now</a>
    </div>
</div>
{% endfor %}
```

# 10. Images Daynamic <a href="" name="image_dy"> - </a>

### home > views.py -

```python
def index(request):      
    product_latest = Product.objects.filter(featured=False).order_by('-id')[:4]
    product_pick = Product.objects.filter(featured=False).order_by('?')[:4]
    context = {
        'product_latest': product_latest,
        'product_pick': product_pick,
    }
    return render(request, 'index.html', context)
```

### home > templates > content.html -

```html
{% for pick in product_pick %}
<div class="col-md-3 col-sm-6 col-xs-6">
    <div class="product product-single">
        <div class="product-thumb">
            <a href="/product/{{ pick.id }}/{{ pick.slug }}" class="main-btn quick-view">
                <i class="fa fa-search-plus"></i> Quick view
            </a>
            <img src="{{ pick.image.url }}" height="360px" alt="">
        </div>
        <div class="product-body">
            <h3 class="product-price">${{ pick.price }}</h3>
            <h2 class="product-name">
                <a href="/product/{{ pick.id }}/{{ pick.slug }}">
                    {{ pick.title|truncatewords:"5" }}
                </a>
            </h2>
            <div class="product-btns">
                <button class="main-btn icon-btn"><i class="fa fa-heart"></i></button>
                <button class="main-btn icon-btn"><i class="fa fa-exchange"></i></button>
                <a href="/addtocart/{{ random.id }}" class="primary-btn add-to-cart">
                    <i class="fa fa-shopping-cart"></i> Add to Cart
                </a>
            </div>
        </div>
    </div>
</div>
{% endfor %}

[ Apply Same Code In The Latest Post & Other ]
```

# 11. Category Products <a href="" name="ca-products"> - </a>

### home > templates > create file -

- > category.html -

### home > views.py -

```python
def category(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category.html', context)
```

### home > templates > category.html -

```html
<!-- STORE -->
<div id="store">
    <!-- row -->
    <div class="row">
        {% for product in products %}
        <!-- Product Single -->
        <div class="col-md-4 col-sm-6 col-xs-6">
            <div class="product product-single">
                <div class="product-thumb">
                    <a href="/product/{{ product.id }}/{{ product.slug }}" class="main-btn quick-view">
                        <i class="fa fa-search-plus"></i> Quick view
                    </a>
                    <img src="{{ product.image.url }}" height="360px" alt="">
                </div>
                <div class="product-body">
                    <h3 class="product-price">$ {{ product.price }}</h3>
                    <h2 class="product-name">
                        <a href="/product/{{ product.id }}/{{ product.slug }}">
                            {{ product.title|truncatewords:"5" }}
                        </a>
                    </h2>
                    <div class="product-btns">
                        <button class="main-btn icon-btn"><i class="fa fa-heart"></i></button>
                        <button class="main-btn icon-btn"><i class="fa fa-exchange"></i></button>
                        <a href="" class="primary-btn add-to-cart">
                            <i class="fa fa-shopping-cart"></i> Addto Cart
                        </a>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
        <!-- /Product Single -->
    </div>
    <!-- /row -->
</div>
```

# 12. Search Products <a href="" name="search"> - </a>

### home > create file -

- > forms.py -
- > templates 
    - > search.html

### home > forms.py -

```python
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()
```

### home > views.py -

```python
from django.db.models import Q
from .forms import SearchForm

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter( title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {
                'products': products,
                'query': query,
                'category': category,
            }
            return render(request, 'search.html', context)

    return HttpResponseRedirect('/')
```

### ecommerce > urls.py -

```python
urlpatterns = [
    path('search/', home.search, name='search'),
]
```

### home > templates > header.html -

{% load mptt_tags %}

```html
<!-- Search -->
<div class="header-search">
    <form action="/search/" method="POST">
        {% csrf_token %}
        <input id="query" name="query" class="input search-input" type="text" placeholder="Enter your keyword">
        <select name="catid" class="input search-categories">
            <option value="0">All Categories</option>
            {% recursetree category %}
                {% if node.is_leaf_node %}
                    <option value="{{ node.id }}">{{ node.title }}</option>
                {% endif %}
                {% if not node.is_leaf_node %}
                    <optgroup label="{{ node.title }}">{{ children }}</optgroup>
                {% endif %}
            {% endrecursetree %}
        </select>
        <button class="search-btn"><i class="fa fa-search"></i></button>
    </form>
</div>
<!-- /Search -->
```

### home > templates > search.html -

```html
{% block title %} Eshop.com : {{ query }} results {% endblock %}

{% block content %}

<!-- BREADCRUMB -->
<li class="active">{{ query }} Result </li>

<!-- STORE -->
<div id="store">
    <!-- row -->
    <div class="row">
        <div class="col-md-12">
            <div class="order-summary clearfix">
                <div class="section-title">
                    <h3 class="title">Product List</h3>
                </div>
                <table class="shopping-cart-table table">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th></th>
                            <th>Category</th>
                            <th class="text-center">Price</th>
                            <th class="text-center">Quantity</th>
                            <th class="text-right"></th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for product in products %}
                        <tr>
                            <td class="thumb">
                                <a href="/product/{{ product.id }}/{{ product.slug }}">
                                    <img src="{{ product.image.url }}" alt="" style="height: 100px">
                                </a>
                            </td>
                            <td class="details">
                                <a href="/product/{{ product.id }}/{{ product.slug }}">
                                    {{ product.title }}
                                </a>
                            </td>
                            <td class="details"> 
                                <a href="/category/{{ product.category_id }}/{{ product.category.slug }}">
                                    {{ product.category }}
                                </a>
                            </td>
                            <td class="price text-center"> <strong>{{ product.price}}</strong> </td>
                            <td class="qty text-center"><input class="input" type="number" value="1"></td>
                            <td class="text-right">
                                <a href="/order/addtoshopcart/{{ rs.id }}" class="primary-btn add-to-cart">
                                    <i class="fa fa-shopping-cart"></i> Add to Cart
                                </a>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <!-- /row -->
</div>
<!-- /STORE -->
{% endblock %}
```

# 13. Auto Search Complete Ajax <a href="" name="autosearch"> - </a>

### home > templates > css.html -

```html
<!-- jQuery UI !-->
<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">

<!-- jQuery Plugins -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"> </script>

<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>


[Delete jQuery on Scripts.html file]
```

### home > views.py -

```python
import json

def searchAuto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for product in products:
            product_json = {}
            product_json = product.title + " > " + product.category.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
```

### ecommerce > urls.py -

```python
urlpatterns = [
    path('search_auto/', home.searchAuto, name='search_auto'),
]
```

### home > templates > header.html -


```html
<script>
    $(function () {
        $("#query").autocomplete({
            source: "/search_auto/",
            select: function (event, ui) { 
                AutoCompleteSelectHandler(event, ui)
            },
            minLength: 2,
        });
    });
    function AutoCompleteSelectHandler(event, ui) {
        var selectedObj = ui.item;
    }
</script>
```

[ Must use search form 'id=query' ]



# 14. Single Page Dynamic <a href="" name="single"> - </a>

### home > views.py -

```python
def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(id=id)
    product_random = Product.objects.filter(featured=False).order_by('?')[:4]
    images = Images.objects.filter(product_id=id)
    context = {
        'category': category,
        'product': product,
        'images': images,
        'product_random': product_random,
    }
    return render(request, 'product_detail.html', context)
```

### ecommerce > urls.py -

    urlpatterns = [
        path('product/<int:id>/<slug:slug>', home.product_detail, name='product'),
    ]


### home > templates > create a file -

- > product-detail.html -

```html
{% block title %} {{ product.title }} {% endblock %}

{% block keywords %} {{ product.keywords }} {% endblock %}

{% block description %} {{ product.description }} {% endblock %}

{% block content %}

<!-- BREADCRUMB -->
<li><a href="{% url 'index' %}">Home</a></li>
<li><a href="/category/{{ product.category.id }}/{{ product.category.slug }}">
    {{ product.category.title }}
</a>
</li>
<li class="active">{{ product.title }}</li>

<!-- /BREADCRUMB -->

<div class="col-md-6">
    <div id="product-main-view">
        <div class="product-view">
            <img src="{{ product.image.url }}" alt="">
        </div>
        {% for image in images %}
        <div class="product-view">
            <img src="{{ image.image.url }}" alt="">
        </div>
        {% endfor %}
    </div>
    <div id="product-view">
        <div class="product-view">
            <img src="{{ product.image.url }}" alt="">
        </div>
        {% for image in images %}
        <div class="product-view">
            <img src="{{ image.image.url }}" alt="">
        </div>
        {% endfor %}
    </div>
</div>

<div class="col-md-6">
    <div class="product-body">
        <div class="product-label">
            <span>New</span>
            <span class="sale">-20%</span>
        </div>
        <h2 class="product-name">{{ product.title }}</h2>
        <h3 class="product-price">$ {{ product.price }} </h3>
        <p><strong>Brand:</strong> E-SHOP</p>
        <p>{{ product.description }}</p>
    </div>
</div>
<div class="tab-content">
    <div id="tab1" class="tab-pane fade in active">
        <p>{{ product.details|safe }}</p>
    </div>
</div>

{% endblock %}
```

# 15. Single Page Comments <a href="" name="comments"> - </a>

### product > models.py -

```python
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=400, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

```

### product > admin.py -

```python
class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('__str__', 'comment','subject', 'ip', 'user', 'product', 'rate', 'id')

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate

### product > views.py -

```python
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from product.models import CommentForm, Comment

def addComment(request, id):
url = request.META.get('HTTP_REFERER')
if request.method == 'POST': 
    form = CommentForm(request.POST)
    if form.is_valid():
        data = Comment()
        data.subject = form.cleaned_data['subject']
        data.comment = form.cleaned_data['comment']
        data.rate = form.cleaned_data['rate']
        data.ip = request.META.get('REMOTE_ADDR')
        data.product_id = id
        current_user = request.user
        data.user_id = current_user.id
        data.save()  
        messages.success(
            request, "Your review has been sent. Thank you for your interest.")
        return HttpResponseRedirect(url)

return HttpResponseRedirect(url)
```

### product > urls.py -

```python
from django.urls import path
from .import views

urlpatterns = [
    path('addcomment/<int:id>', views.addComment, name='addcomment'),
]
```

### home > views.py -

```python
from product.models import Comment, CommentForm

def productDetail(request, id, slug):
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {
        'comments': comments,
    }
    return render(request, 'product-detail.html', context)
```

### home > templates > product-detail.html -

```django
<div class="col-md-12">
    <div class="product-tab">
        <div class="tab-content">
            <div id="tab2" class="tab-pane fade in">
                <div class="row">
                    <div class="col-md-6">
                        <div class="product-reviews">
                            {% for comment in comments %}
                            <div class="single-review">
                                <div class="review-heading">
                                    <div><a href="#"><i class="fa fa-user-o"></i> {{ comment.user.first_name }}</a></div>
                                    <div><a href="#"><i class="fa fa-clock-o"></i> {{ comment.create_at }}</a></div>	
                                    <div class="review-rating pull-right">
                                        <i class="fa fa-star {% if comment.rate < 1 %}-o empty {% endif %}"></i>
                                        <i class="fa fa-star {% if comment.rate < 2 %}-o empty {% endif %}"></i>
                                        <i class="fa fa-star {% if comment.rate < 3 %}-o empty {% endif %}"></i>
                                        <i class="fa fa-star {% if comment.rate < 4 %}-o empty {% endif %}"></i>
                                        <i class="fa fa-star{% if comment.rate < 5 %}-o empty {% endif %}"></i>
                                    </div>
                                </div>
                                <div class="review-body">
                                    <p> <b> {{ comment.subject }}</b></p>
                                </div>
                                <div class="review-body">
                                    <p>{{ comment.comment }}</p>
                                </div>
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                    <div class="col-md-6">
                        <h4 class="text-uppercase">Write Your Review</h4>
                        <form class="review-form" action="/product/addcomment/{{ product.id }}" method="post">
                            {% csrf_token %}
                            <div class="form-group">
                                <input class="input" name="subject" type="text" placeholder="Your Subject" />
                            </div>
                            <div class="form-group">
                                <textarea class="input" name="comment" placeholder="Your review"></textarea>
                            </div>
                            <div class="form-group">
                                <div class="input-rating">
                                    <strong class="text-uppercase">Your Rating: </strong>
                                    <div class="stars">
                                        <input type="radio" id="star5" name="rate" value="5" />
                                        <label for="star5"></label>
                                        <input type="radio" id="star4" name="rate" value="4" />
                                        <label for="star4"></label>
                                        <input type="radio" id="star3" name="rate" value="3" />
                                        <label for="star3"></label>
                                        <input type="radio" id="star2" name="rate" value="2" />
                                        <label for="star2"></label>
                                        <input type="radio" id="star1" name="rate" value="1" />
                                        <label for="star1"></label>
                                    </div>
                                </div>
                            </div>
                            {% if user.id is not None %}
                            <button class="primary-btn">Submit</button>
                            {% else %}
                            <p>You must be Logged in to post a review</p>
                            {% endif %}
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

# 16. Add & Delete Cart <a href="" name="cart"> - </a>

### Command Prompt -

- > python manage.py startapp order

### ecommerce > settings.py -

```python
INSTALLED_APPS = [
    'order.apps.OrderConfig', 
]
```

### ecommerce > urls.py -

```python
urlpatterns = [
    path('order/', include('order.urls')),
]
```

### order > create file & folder -

- > urls.py
- > templates
    - > shopcart_product.html


### order > models.py -

```python
from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.forms import ModelForm

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
```

### order > admin.py -

```python
from django.contrib import admin
from . models import ShopCart


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']

    class Meta:
        model = ShopCart

admin.site.register(ShopCart, ShopCartAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate

### order > views.py -

```python
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from order.models import ShopCart, ShopCartForm
from product.models import Category, Product


@login_required(login_url='/login')
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(product_id=id)

    if checkproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        return HttpResponseRedirect(url)
    
    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for cart in shopcart:
        total += cart.product.price * cart.quantity

    context = {
        'category': category,
        'shopcart': shopcart,
        'total': total,
    }
    return render(request, 'shopcart_product.html', context)


@login_required(login_url='/login')
def deleteshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect(url)

```

### order > urls.py -

```python
from django.urls import path
from . import views

urlpatterns = [
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deleteshopcart/<int:id>', views.deleteshopcart, name='deleteshopcart'),
]
```

### ecommerce > urls.py -

```python
from order import views as order

urlpatterns = [
    path('shopcart/', order.shopcart, name='shopcart'),
]
```

### order > templates > shopcart_product.html -

```django
{% block title %} Shop Cart {% endblock %}

{% block content %}

<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="col-md-12">
                <div class="order-summary clearfix">
                    <div class="section-title">
                        <h3 class="title">Shop Cart Product List</h3>
                    </div>
                    <table class="shopping-cart-table table">
                        <thead>
                            <tr>
                                <th>Product</th>
                                <th></th>
                                <th class="text-center">Price</th>
                                <th class="text-center">Quantity</th>
                                <th class="text-center">Total</th>
                                <th class="text-right"></th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for cart in shopcart %}
                            <tr>
                                <td class="thumb"><img src="{{ cart.product.image.url }}" alt=""></td>
                                <td class="details">
                                    <a href="/product/{{ cart.product.id }}/{{ cart.product.slug }}">
                                        {{ cart.product.title }}
                                    </a>
                                </td>
                                <td class="price text-center"><strong>${{ cart.product.price }}</strong></td>
                                <td class="qty text-center"><strong>{{cart.quantity}}</strong></td>
                                <td class="total text-center">
                                    <strong class="primary-color">${{ cart.amount }}</strong>
                                </td>
                                <td class="text-right">
                                    <a href="/order/deleteshopcart/{{ cart.id }}" 
                                    onclick="return confirm('Delete ! Are you sure?')" class="main-btn icon-btn">
                                        <i class="fa fa-close"></i>
                                    </a>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                        <tfoot>
                            <tr>
                                <th class="empty" colspan="3"></th>
                                <th>SUBTOTAL</th>
                                <th colspan="2" class="sub-total">${{ total }}</th>
                            </tr>
                            <tr>
                                <th class="empty" colspan="3"></th>
                                <th>SHIPING</th>
                                <td colspan="2">Free Shipping</td>
                            </tr>
                            <tr>
                                <th class="empty" colspan="3"></th>
                                <th>TOTAL</th>
                                <th colspan="2" class="total">${{ total }}</th>
                            </tr>
                        </tfoot>
                    </table>
                    <div class="pull-right">
                        <button class="primary-btn">Place Order</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% endblock %}


{% block scripts %} {% endblock %}
```

### home > templates > content.html -

```html
<a href="/order/addtoshopcart/{{ latest.id }}" class="primary-btn add-to-cart">
    <i class="fa fa-shopping-cart"></i> Add to Cart
</a>

[ Add this href location to all 'Add to Cart' link ]
```

### home > templates > header.html -

```html
<!-- Cart -->
<li class="header-cart dropdown default-dropdown">
    <a href="/shopcart/">
        <div class="header-btns-icon">
            <i class="fa fa-shopping-cart"></i>
            <span class="qty">3</span>
        </div>
    </a>
</li>
<!-- /Cart -->
```

### home > templates > product-detail.html -

```django
<div class="product-btns">
    <form action="/order/addtoshopcart/{{ product.id }}" method="post">
        {% csrf_token %}
        <div class="qty-input">
            <span class="text-uppercase">QTY: </span>
            <input name="quantity" class="input" type="number" value="1" min="1"
                max="{{ product.amount }}">
        </div>
        <button type="submit" class="primary-btn add-to-cart"><i
                class="fa fa-shopping-cart"></i> Add to Cart
        </button>
    </form>
</div>
```

### home > templates > search.html -

```django
<td class="text-right">
    <a href="/order/addtoshopcart/{{ product.id }}" class="primary-btn add-to-cart">
        <i class="fa fa-shopping-cart"></i>Add to 
    </a>
</td>
```

# 17. User Model & Login <a href="" name="login"> - </a>

### Command Prompt -

- > python manage.py startapp user

### ecommerce > settings.py -

```python
INSTALLED_APPS = [
    'user.apps.UserConfig', 
]
```

### ecommerce > urls.py -

```python
from user import views as user

urlpatterns = [
    path('login/', user.loginUser, name='login'),
    path('signup/', user.signupUser, name='signup'),
    path('logout/', user.logoutUser, name='logout'),
]
```

### user > create file & folder -

- > urls.py
- > templates
    - > login.html
    - > signup.html

### user > models.py -

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        
    image_tag.short_description = 'Image'

```

### user > admin.py -

```python
from django.contrib import admin
from user.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'phone', 'city', 'country', 'image_tag']


admin.site.register(UserProfile, UserProfileAdmin)
```
    
### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate


### user > views.py -

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from product.models import Category
from . models import UserProfile


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')


def signupUser(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'signup.html', context)

```

### user > templates > login.html -

```html
{% block title %} User Login {% endblock %}

{% block content %} 


<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">

            <div class="col-md-6 col-lg-offset-3">
                <div class="billing-details">

                    <div class="section-title">
                        <h3 class="title">Login Form</h3>
                    </div>
                    <form action="" method="POST">
                        {% csrf_token %}
                        <div class="form-group">
                            <input class="input" type="text" name="username" placeholder=" User Name">
                        </div>
                        <div class="form-group">
                            <input class="input" type="password" name="password" placeholder="Password">
                        </div>
                        <input class="btn btn-info" type="submit" value="Login">
                    </form>

                </div>
            </div>


        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% endblock %}
```

### home > templates > header.html -

```django
<!-- Account -->
<li class="header-account dropdown default-dropdown">
    {% if user.id is not None %}
    <div class="dropdown-toggle" role="button" data-toggle="dropdown" aria-expanded="true">
        <div class="header-btns-icon">
            <img src="{{ request.session.userimage }}" style="height: 40px;" alt="">
        </div>
        <strong class="text-uppercase">{{ user.first_name }} <i class="fa fa-caret-down"></i></strong>
    </div>
    {% else %}
    <div>
        <div class="header-btns-icon">
            <i class="fa fa-user-o"></i>
        </div>
        <a href="/login" class="text-uppercase">Login</a> / <a href="/signup"
            class="text-uppercase">Join</a>
        <div>
            <p>Welcome</p>
        </div>
    </div>
    {% endif %}
    <ul class="custom-menu">
        <li><a href="/logout"><i class="fa fa-unlock-alt"></i> Logout</a></li>
    </ul>
</li>
<!-- /Account -->
```

# 18. Sign Up Form <a href="" name="signup"> - </a>

### user > Create a file -

- > forms.py -

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='User Name: ')
    email = forms.EmailField(max_length=200, label='Email: ')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name: ')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name: ')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

```

### user > views.py -

```python
from .forms import SignUpForm

def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    form = SignUpForm
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup.html', context)
```

### user > templates > signup.html -

```django
{% load crispy_forms_tags %}

{% block title %} Signup User {% endblock %}

{% block content %}

<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="col-md-6 col-lg-offset-3">
                <div class="billing-details">
                    <div class="section-title">
                        <h3 class="title">Sign Up Form</h3>
                    </div>
                    {{ form.media }}
                        <form action="" method="POST" enctype="multipart/form-data">
                        {% csrf_token %}
                        {{ form|crispy }}
                        <input class="btn btn-info" type="submit" value="Signup">
                    </form>
                        <input class="btn btn-info" type="submit" value="Signup">
                    </form>

                </div>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% endblock %}

{% block scripts %} {% endblock %}
```

# 19. User Account Page <a href="" name="myaccount"> - </a>


### user > templates > Create file -

- > user_profile.html
- > user_panel.html

### user > views.py -

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category': category,
        'profile': profile,
    }
    return render(request, 'profile.html', context)
```

### user > urls.py -

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
]
```

### user > templates > user_panel.html -

```html
<div class="billing-details">
    <div class="section-title">
        <h3 class="title">User Panel</h3>
    </div>
    <div class="aside">
        <ul class="list-links">
            <li><a href="/user">User Profile</a></li>
            <li><a href="/user/orders">My Orders</a></li>
            <li><a href="/user/orders_product">My Order Product</a></li>
            <li><a href="/user/comments">My Comments</a></li>
            <li><a href="/user/favorits">My Favorits</a></li>
            <li><a href="/user/products">My Products</a></li>
            <li><a href="/logout">Logout</a></li>
        </ul>
    </div>
</div>
```

### user > templates > user_profile.html -


```django
{% block title %} {{ user.first_name }} Profile {% endblock %}

{% block content %}

<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">

            <div class="col-md-3">
                {% include "user_panel.html" %}
            </div>

            <div class="col-md-9">
                <div class="billing-details">
                    <div class="section-title">
                        <h3 class="title">User Profile Info.</h3>
                    </div>
                </div>
                <table class="shopping-cart-table table">
                    <tr>
                        <th class="text-left">
                            <a href="/user/update" class="primary-btn">Update Profile</a>
                            <a href="/user/password" class="primary-btn">Change Password</a>
                        </th>
                        <td><img src="{{ profile.image.url }}" style="border-radius: 45px; height: 200px "></td>
                    </tr>
                    <tr>
                        <th class="text-left">Name Surname</th>
                        <td class="text-left">{{ user.first_name}} {{ user.last_name}} </td>
                    </tr>
                    <tr>
                        <th class="text-left">Email</th>
                        <td class="text-left">{{ profile.user.email}}</td>
                    </tr>
                    <tr>
                        <th class="text-left">Phone</th>
                        <td class="text-left">{{ profile.phone}}</td>
                    </tr>
                    <tr>
                        <th class="text-left">Addres</th>
                        <td class="text-left">{{ profile.address}}</td>
                    </tr>
                    <tr>
                        <th class="text-left">City</th>
                        <td class="text-left">{{ profile.city}}</td>
                    </tr>
                    <tr>
                        <th class="text-left">Country</th>
                        <td class="text-left">{{ profile.country}}</td>
                    </tr>

                </table>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% endblock %}
```


### user > templates > header.html -

```html
<!-- Account -->
<ul class="custom-menu">
    <li><a href="/user"><i class="fa fa-user-o"></i> My Account</a></li>
    <li><a href="/user/favorits"><i class="fa fa-heart-o"></i> My Favorits</a></li>
    <li><a href="/user/orders"><i class="fa fa-exchange"></i> My Order </a></li>
    <li><a href="/user/comments"><i class="fa fa-check"></i> My Comments </a></li>
    <li><a href="/logout"><i class="fa fa-unlock-alt"></i> Logout</a></li>
</ul>
```

# 20. Update User Profile <a href="" name="update"> - </a>

### user > forms.py -

```python
from django.contrib.auth.forms import UserChangeForm
from django.forms import TextInput, EmailInput, Select, FileInput
from user.models import UserProfile

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'email': EmailInput(attrs={'placeholder': 'email'}),
            'first_name': TextInput(attrs={'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'placeholder': 'last_name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'placeholder': 'phone'}),
            'address': TextInput(attrs={'placeholder': 'address'}),
            'city': TextInput(attrs={'placeholder': 'city'}),
            'country': TextInput(attrs={'placeholder': 'country'}),
            'image': FileInput(attrs={'placeholder': 'image', }),
        }
```

### user > views.py -

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)
```

### user > urls.py -

```python
urlpatterns = [
    path('update/', views.user_update, name='user_update'),
]
```

### user > templates > Create file -

- > user_update.html -

```django
{% block title %} {{ user.first_name }} Profile {% endblock %}

{% load crispy_forms_tags %}

{% block content %}

<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">

            <div class="col-md-3">
                {% include "user_panel.html" %}
            </div>

            <div class="col-md-9">
                <div class="billing-details">
                    <div class="section-title">
                        <h3 class="title">User Profile Update</h3>
                    </div>
                </div>
                {{ form.media }}
                <form method="POST" enctype="multipart/form-data">
                    {% csrf_token %}
                    <fieldset class="form-group">
                        {{ user_form|crispy  }}
                        {{ profile_form|crispy  }}
                    </fieldset>
                    <div class="form-group">
                        <button class="primary-btn" type="submit">Update</button>
                    </div>
                </form>

            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% endblock %}
```


# 21. User Password Change <a href="" name="password"> - </a>

### user > views.py -

```python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required(login_url='/login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,  
            'category': category,
        }
        return render(request, 'user_password.html', context)
```

### user > urls.py -

```python
urlpatterns = [
    path('password/', views.user_password, name='user_password'),
]
```

### user > templates > create file -

- > user_password.html -

```django
{% load crispy_forms_tags %}

{% block title %} {{ user.first_name }} Change Password {% endblock %}


{% block content %}

    <!-- section -->
    <div class="section">
        <!-- container -->
        <div class="container">
            <!-- row -->
            <div class="row">

                <div class="col-md-3">
                    {% include "user_panel.html" %}
                </div>

                <div class="col-md-9">
                    <div class="billing-details">
                        <div class="section-title">
                            <h3 class="title">User Change Password</h3>
                        </div>
                    </div>
                    {{ form.media }}
                    <form method="POST" enctype="multipart/form-data">
                        {% csrf_token %}
                        {{ form|crispy }}
                        <button class="primary-btn" type="submit">Save changes</button>
                    </form>

                </div>
            </div>
            <!-- /row -->
        </div>
        <!-- /container -->
    </div>
    <!-- /section -->

{% endblock %}
```

# 22. Order Form & Complete It <a href="" name="ordercomplete"> - </a>

### order > templates > create file -

- > Order_Form.html
- > Order_Completed.html

### order > models.py -

```python
from django.contrib.auth.models import User
from product.models import Product
from django.forms import ModelForm


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
```

### order > admin.py -

```python
from . models import ShopCart, Order, OrderProduct

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user',  'first_name',  'last_name', 'address', 'city', 'country', 'ip', 'phone', 'total')
    can_delete = False
    inlines = [OrderProductline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']

    class Meta:
        model = OrderProduct

admin.site.register(OrderProduct, OrderProductAdmin)
```

### order > views.py -

```python
from . models import OrderForm, Order, OrderProduct
from django.utils.crypto import get_random_string
from user.models import UserProfile

def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for shop in shopcart:
        total += shop.product.price * shop.quantity

    if request.method == 'POST': 
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            for shop in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = shop.product_id
                detail.user_id = current_user.id
                detail.quantity = shop.quantity
                detail.price = shop.product.price
                detail.amount = shop.amount
                detail.save()
                product = Product.objects.get(id=shop.product_id)
                product.amount -= shop.quantity
                product.save()
            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order has been completed. Thank you ")
            context = {
                'ordercode': ordercode,
                'category': category
            }
            return render(request, 'Order_Completed.html', context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
            'category': category,
            'total': total,
            'form': form,
            'profile': profile,
            }
    return render(request, 'Order_Form.html', context)
```

### order > urls.py -

```python
urlpatterns = [
    path('orderproduct/', views.orderproduct, name='orderproduct'),
]
```

### order > templates > shopcart_product.html -

```django
<div class="pull-right">
    <a href="{% url 'orderproduct' %}" class="primary-btn">Place Order</a>
</div>
```

### order > templates > Order_Form.html -

```django
{% block title %} Order Page {% endblock %}

{% block content %}

<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <form action="" method="POST">
                {% csrf_token %}
                <div class="col-md-6">
                    <div class="billing-details">
                        <p>Already a customer ? <a href="/login">Login</a></p>
                        <div class="section-title">
                            <h4 class="title">Shipping Details</h4>
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">First name:</label>
                            <input type="text" name="first_name" value="{{ user.first_name }}" class="input"
                                maxlength="10" required id="id_first_name">
                        </div>
                        <div class="form-group">
                            <label for="id_last_name">Last name:</label>
                            <input type="text" name="last_name" value="{{ user.last_name }}" class="input"
                                maxlength="10" required id="id_last_name">
                        </div>
                        <div class="form-group">
                            <label for="id_address">Address:</label>
                            <input type="text" name="address" value="{{ profile.address }}" class="input"
                                maxlength="150" id="id_address">
                        </div>
                        <div class="form-group">
                            <label for="id_phone">Phone:</label>
                            <input type="text" name="phone" value="{{ profile.phone }}" class="input" maxlength="20"
                                id="id_phone">
                        </div>
                        <div class="form-group">
                            <label for="id_city">City:</label>
                            <input type="text" name="city" class="input" id="id_city"
                                value="{{ profile.city }}">
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">Country :</label>
                            <input type="text" name="country" class="input" id="id_country"
                                value="{{ profile.country }}">
                        </div>
                        <div class="pull-right">
                            <button type="submit" class="primary-btn">Complete Order</button>
                        </div>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="shiping-methods">
                        <div class="section-title">
                            <h4 class="title">Payment Information</h4>
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">Total: {{ total }} USD </label>
                            <input type="text" name="total" class="input" readonly
                                value="${{ total }}">
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">Credit Card Holder</label>
                            <input type="text" name="holder" class="input" value="">
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">Credit Card Number</label>
                            <input type="text" name="number" class="input" value="">
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">Credit Exp Date/Year</label>
                            <input type="text" name="ecpdate" class="input" placeholder="mm/yy">
                        </div>
                        <div class="form-group">
                            <label for="id_first_name">Security Number</label>
                            <input type="text" name="secnumber" class="input" value="">
                        </div>
                    </div>
                </div>

            </form>

            <div class="col-md-12">
                <div class="order-summary clearfix">
                    <div class="section-title">
                        <h3 class="title">Shopcart Product List</h3>
                    </div>
                    <table class="shopping-cart-table table">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Product</th>
                                <th class="text-center">Price</th>
                                <th class="text-center">Quantity</th>
                                <th class="text-center">Total</th>
                            </tr>
                        </thead>
                        <tbody>

                            {% for shop in shopcart %}
                            <tr>
                                <td class="thumb">
                                    <img src="{{shop.product.image.url}}" alt="">
                                </td>
                                <td class="details">
                                    <a href="/product/{{ shop.product.id }}/{{ shop.product.slug }}">{{shop.product}}</a>
                                </td>
                                <td class="price text-center">
                                    <strong>${{ shop.product.price }}</strong>
                                </td>
                                <td class="qty text-center">
                                    <strong>{{shop.quantity}}</strong>
                                </td>
                                <td class="total text-center">
                                    <strong class="primary-color">${{ shop.amount }}</strong>
                                </td>
                            </tr>

                            {% endfor %}

                        </tbody>
                        <tfoot>
                            <tr>
                                <th class="empty" colspan="3"></th>
                                <th>SUBTOTAL</th>
                                <th colspan="2" class="sub-total">${{ total }}</th>
                            </tr>
                            <tr>
                                <th class="empty" colspan="3"></th>
                                <th>SHIPING</th>
                                <td colspan="2">Free Shipping</td>
                            </tr>
                            <tr>
                                <th class="empty" colspan="3"></th>
                                <th>TOTAL</th>
                                <th colspan="2" class="total">${{ total }}</th>
                            </tr>
                        </tfoot>
                    </table>

                </div>

            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% endblock %}
```

### order > templates > Order_Completed.html -

```django
{% block title %} Order Complete {% endblock %}

{% block content %}

    <!-- section -->
    <div class="section">
        <!-- container -->
        <div class="container">
            <!-- row -->
            <div class="row">

                <div class="col-md-12">
                    <div class="order-summary clearfix">
                        <div class="section-title">
                            <h3 class="title">Order Complated</h3>
                        </div>
                        <hr>
                        <h2>Dear  {{ user.first_name }} {{  user.last_name }}</h2>
                        <hr>
                        <h3>Your order is completed</h3>
                        <h3>Order Code : {{ ordercode }}</h3>
                        <h3>Thank You</h3>
                        <hr>

                    </div>

                </div>


            </div>
            <!-- /row -->
        </div>
        <!-- /container -->
    </div>
    <!-- /section -->

{% endblock %}
```

# 23. User Order & Order Details <a href="" name="orderdetail"> - </a>

### user > templates > create files -

- > user_orders.html
- > user_order_products.html
- > user_order_detail.html

### user > views.py -

```python
from order.models import Order, OrderProduct

@login_required(login_url='/login')
def user_orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'orders': orders,
    }
    return render(request, 'user_orders.html', context)


@login_required(login_url='/login')
def user_orderdetail(request, id):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        'category': category,
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'user_order_detail.html', context)


@login_required(login_url='/login')
def user_order_product(request):
    category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(
        user_id=current_user.id).order_by('-id')
    context = { 
        'category': category,
        'order_product': order_product,
    }
    return render(request, 'user_order_products.html', context)


@login_required(login_url='/login')
def user_order_product_detail(request, id, oid):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    context = {
        'category': category,
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'user_order_detail.html', context)
```

### user > urls.py -

```python
urlpatterns = [
    path('orders/', views.user_orders, name='user_orders'),
    path('orders_product/', views.user_order_product, name='user_order_product'),
    path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),
]
```

### user > templates > user_orders.html -

```django
<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="col-md-3">
                {% include "user_panel.html" %}
            </div>

            <div class="col-md-9">
                <div class="order-summary clearfix">
                    <div class="section-title">
                        <h3 class="title">Order List</h3>
                    </div>
                    <table class="shopping-cart-table table">
                        <tr>
                            <th class="text-left">Id </th>
                            <th class="text-left">First Name </th>
                            <th class="text-left">Last Name </th>
                            <th class="text-left">Total </th>
                            <th class="text-left">Status </th>
                            <th class="text-left">Date </th>
                            <th class="text-left">Detail </th>
                        </tr>
                        {% for order in orders %}
                            <tr>
                                <td class="text-left">{{ order.id}} </td>
                                <td class="text-left">{{ order.first_name}} </td>
                                <td class="text-left">{{ order.last_name}} </td>
                                <td class="text-left">{{ order.total}} </td>
                                <td class="text-left">{{ order.status}} </td>
                                <td class="text-left">{{ order.create_at}} </td>
                                <td class="text-left">
                                    <a class="primary-btn"href="/user/orderdetail/{{ order.id }}"> Detail </a>
                                </td>
                            </tr>
                        {% endfor %}
                    </table>

                </div>

            </div>


        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->
```

### user > templates > user_order_detail.html -

```django
<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="col-md-3">
                {% include "user_panel.html" %}
            </div>

            <div class="col-md-9">
                <div class="order-summary clearfix">
                    <div class="section-title">
                        <h3 class="title">Order Detail</h3>
                    </div>
                    <table class="shopping-cart-table table">
                        <tr>
                            <th class="text-left">Name Surname</th>
                            <td class="text-left">{{ order.first_name }} {{ order.last_name }} </td>
                        </tr>
                        <tr>
                            <th class="text-left">Phone</th>
                            <td class="text-left">{{ order.phone }}</td>
                        </tr>
                        <tr>
                            <th class="text-left">Addres</th>
                            <td class="text-left">{{ order.address }}</td>
                        </tr>
                        <tr>
                            <th class="text-left">City</th>
                            <td class="text-left">{{ order.city }}</td>
                        </tr>
                        <tr>
                            <th class="text-left">Status</th>
                            <td class="text-left">{{ order.status }}</td>
                        </tr>

                        <tr>
                            <th class="text-left">Date</th>
                            <td class="text-left">{{ order.create_at }}</td>
                        </tr>
                        <tr>
                            <th class="text-left">Shipping Inf.</th>
                            <td class="text-left">{{ order.adminnote }}</td>
                        </tr>

                    </table>

                    <div class="section-title">
                        <h4 class="title">Order Item List</h4>
                    </div>

                    <table class="shopping-cart-table table">
                        <tr>
                            <th class="text-left"></th>
                            <th class="text-left">Product Name </th>
                            <th class="text-left">Price </th>
                            <th class="text-left">Qauatity </th>
                            <th class="text-left">Amount </th>
                            <th class="text-left">Status </th>
                            <th class="text-left">Date </th>
                        </tr>
                        {% for orderitem in orderitems %}
                            <tr>
                                <td class="text-left">
                                    <a href="/product/{{ orderitem.product_id }}/{{ orderitem.product.slug }}">
                                        <img src="{{orderitem.product.image.url}}" alt=""
                                            style="height: 50px; width: 50px;">
                                    </a>
                                </td>
                                <td class="text-left">{{ orderitem.product.title|truncatewords:"7"}}</td>
                                <td class="text-left">{{ orderitem.price}} </td>
                                <td class="text-left">{{ orderitem.quantity}} </td>
                                <td class="text-left">{{ orderitem.amount}} </td>
                                <td class="text-left">{{ orderitem.status}} </td>
                                <td class="text-left">{{ orderitem.create_at|timesince}} </td>
                            </tr>
                        {% endfor %}

                    </table>

                </div>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->
```

### user > templates > user_order_products.html -

```django
<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="col-md-2">
                {% include "user_panel.html" %}
            </div>

            <div class="col-md-10">
                <div class="order-summary clearfix">
                    <div class="section-title">
                        <h3 class="title">Order Product List</h3>
                    </div>

                    <table class="shopping-cart-table table">
                        <tr>
                            <th class="text-left"> </th>
                            <th class="text-left">Product Name </th>
                            <th class="text-left">Price </th>
                            <th class="text-left">Qauatity </th>
                            <th class="text-left">Amount </th>
                            <th class="text-left">Status </th>
                            <th class="text-left">Date </th>
                            <th class="text-left">Detail </th>
                        </tr>
                        {% for order in order_product %}
                            <tr>
                                <td class="text-left">
                                    <a href="/product/{{ order.product_id }}/{{ order.product.slug }}">
                                        <img src="{{order.product.image.url}}" alt="" style="height: 80px">
                                    </a>
                                </td>
                                <td class="text-left">
                                        { order.product.title|truncatewords:"7"}}
                                </td>
                                <td class="text-left">{{ order.price}} </td>
                                <td class="text-left">{{ order.quantity}} </td>
                                <td class="text-left">{{ order.amount}} </td>
                                <td class="text-left">{{ order.status}} </td>
                                <td class="text-left">{{ order.create_at}} </td>
                                <td class="text-left">
                                    <a class="primary-btn"href="/user/order_product_detail/{{ order.id }}/{{ order.order.id}}"> Detail
                                    </a>
                                </td>

                            </tr>
                        {% endfor %}

                    </table>

                </div>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->
```

# 24. User Comment & Delete <a href="" name="comment-delete"> - </a>

### user > templates > create file -

- > user_comments.html

### user > views.py -

```python
from product.models import Comment

def user_comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')
def user_deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')
```

### user > urls.py -

```python
urlpatterns = [
    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
]
```

### user > templates > user_comments.html -

```django
<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="col-md-2">
                {% include "user_panel.html" %}
            </div>
            <div class="col-md-10">
                <div class="section-title">
                    <h4 class="title">User Order List</h4>
                </div>
                <table class="shopping-cart-table table">
                    <tr>
                        <th class="text-left">Product </th>
                        <th class="text-left">Rate </th>
                        <th class="text-left">Subject </th>
                        <th class="text-left">Comment </th>
                        <th class="text-left">Status </th>
                        <th class="text-left">Date </th>
                        <th class="text-left">Detail </th>
                    </tr>
                    {% for comment in comments %}
                        <tr>
                            <td class="text-left">
                                <a href="/product/{{ comment.product_id }}/{{ comment.product.slug }}">
                                    <strong> {{ comment.product.title|truncatewords:"4"}}</strong>
                                </a>
                            </td>
                            <td class="text-left">{{ comment.rate}} </td>
                            <td class="text-left">{{ comment.subject}} </td>
                            <td class="text-left">{{ comment.comment}} </td>
                            <td class="text-left">{{ comment.status}} </td>
                            <td class="text-left">{{ comment.create_at}} </td>
                            <td class="text-left">
                                <a class="primary-btn" href="/user/deletecomment/{{ comment.id }}"
                                    onclick="return confirm('Will be Delete ! Are you sure?')"> Delete </a>
                            </td>
                        </tr>
                    {% endfor %}
                </table>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->
```

# 25. Product Review Avg & Countes <a href="" name="avg-count"> - </a>

### product > models.py -

```python
from django.db.models import Avg, Count

class Product(models.Model):

    **********************************
    **********************************

    def avaregereview(self):
            reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
            avg = 0
            if reviews["avarage"] is not None:
                avg = float(reviews["avarage"])
            return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt
```

### home > templates > product-detail.html -

```html

<div>
    <div class="product-rating">
        <i class="fa fa-star{% if product.avaregereview < 1%}-o empty{% endif%}"></i>
        <i class="fa fa-star{% if product.avaregereview < 2%}-o empty{% endif%}"></i>
        <i class="fa fa-star{% if product.avaregereview < 3%}-o empty{% endif%}"></i>
        <i class="fa fa-star{% if product.avaregereview < 4%}-o empty{% endif%}"></i>
        <i class="fa fa-star{% if product.avaregereview < 5%}-o empty{% endif%}"></i>
        {{ product.avaregereview |stringformat:".2f"}}
    </div>
    <a href="#">{{ product.countreview}} Review(s) / Add Review</a>
</div>
```

### home > templates > content.html & products.html -

```html
[ All the Review are Showing - Paste Here & Change variable name ]

<div class="product-rating">
    <i class="fa fa-star{% if random.avaregereview < 1%}-o empty{% endif%}"></i>
    <i class="fa fa-star{% if product.avaregereview < 2%}-o empty{% endif%}"></i>
    <i class="fa fa-star{% if product.avaregereview < 3%}-o empty{% endif%}"></i>
    <i class="fa fa-star{% if product.avaregereview < 4%}-o empty{% endif%}"></i>
    <i class="fa fa-star{% if product.avaregereview < 5%}-o empty{% endif%}"></i>
    {{ product.avaregereview }} / {{ product.countreview }}
</div>
```

# 26. Frequently Asked Questions <a href="" name="faq"> - </a>

### home > templates > create a file -

- > faq.html

### home > models.py -

```python
class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=400)
    answer = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
```

### home > admin.py -

```python
class FAQAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'ordernumber', 'status']
    list_filter = ['status']
    search_fields = ['__str__']
    list_per_page = 10

    class Meta:
        model = FAQ


admin.site.register(FAQ, FAQAdmin)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate


### home > views.py -

```python
from .models import FAQ

def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter( status="True").order_by("ordernumber")

    context = {
        'category': category,
        'faq': faq,
    }
    return render(request, 'faq.html', context)
```

### ecommerce > urls.py -

```python
urlpatterns = [
    path('faq/', home.faq, name='faq'),
]
```

### home > templates > faq.html -

```django
<!-- section -->
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <div class="section-title">
                <h3 class="title">FAQ</h3>
            </div>
            <div id="accordion">
                {% for ask in faq %}
                    <h3>{{ ask.question }}</h3>
                    <div>
                        <p>
                            {{ ask.answer | safe }}
                        </p>
                    </div>
                {% endfor %}
            </div>

        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>
<!-- /section -->

{% block scripts %} 

<script>
    $(function () {
        $("#accordion").accordion();
    });
</script>

{% endblock %}
```

### home > templates > header.html -

```html
<li><a href="/faq">FAQ</a></li>
```

# 27. Variant Product Setup <a href="" name="variant"> - </a>


> - <a href="#model">1 .Color, Size & Variant Model Create  </a>

> - <a href="#define">2 .Home Views Define  </a>

> - <a href="#pro_intregrate">3. Product Details Page Intregrate </a>

> - <a href="#ord_intregrate">4. Order Page Intregrate </a>

> - <a href="#use_intregrate">5. User Page Intregrate </a>


# 1. Color, Size & Variant Model Create <a href="" name="model"> - </a>

### product > models.py -

```python
from django.utils.safestring import mark_safe

class Product(models.Model):

    VARIANTS = (
            ('None', 'None'),
            ('Size', 'Size'),
            ('Color', 'Color'),
            ('Size-Color', 'Size-Color'),
        )
    
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Variants(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""
```

### Command Prompt -

- > pip install django-admin-thumbnails



### product > admin.py -

```python
import admin_thumbnails

@admin_thumbnails.thumbnail('image')                           
class ProductImageInline(admin.TabularInline):
    readonly_fields = ('id',)                                   


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantsInline]                           


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', '__str__', 'image_thumbnail']


class ColorAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'code', 'color_tag']
    search_fields = ['__str__']


admin.site.register(Color, ColorAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'code']


admin.site.register(Size, SizeAdmin)


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product', 'color', 'size', 'price', 'quantity', 'image_tag']
    search_fields = ['__str__']
    list_filter = ['product']


admin.site.register(Variants, VariantsAdmin)
```

### order > models.py -

```python
from product.models import Variants

class ShopCart(models.Model):

    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def varamount(self):
        return (self.quantity * self.variant.price)


class OrderProduct(models.Model):

    variant = models.ForeignKey(Variants, on_delete=models.SET_NULL, blank=True, null=True)
```

### Command Prompt -

- > python manage.py makemigrations
- > python manage.py migrate
- > python manage.py runserver


### 127.0.0.1:8000/admin > colors & sizes -

    [ Create Color Name & Code of the Varients ]
    [ Create Different Sizes or Categories to Product Varients ]
    [ Create Some Products & Their Varients ]


# 2. Home Views Define <a href="" name="define"> - </a>

### home > views.py -

```python
from django.http import JsonResponse, request
from product.models import Variants
from django.template.loader import render_to_string
from django.db.models import Q, F
from django.db.models.functions import Concat
from django.urls import reverse


def product_detail(request, id, slug):
    query = request.GET.get('q')

    if product.variant != "None":
        if request.method == 'POST':
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id)
            colors = Variants.objects.filter(
                product_id=id, size_id=variant.size_id)
            sizes = Variants.objects.raw(
                'SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
            query += variant.title+' Size:' + str(variant.size) + ' Color:' + str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(
                product_id=id, size_id=variants[0].size_id)
            sizes = Variants.objects.raw(
                'SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
            variant = Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant, 'query': query
                        })
    return render(request, 'product_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)
```

### home > templates > create a file -

- > color_list.html -

```django
<input type="hidden" name="size" id="size" value="{{ size_id }}">
<ul class="color-option" >
    <li><span class="text-uppercase">Color:</span></li>
    {% for color in colors %}
        <input type="radio" name="variantid" id="variantid" value="{{ color.id }}" onchange="this.form.submit();">
        <li >
            <a href="#" style="background-color:{{ color.color.code }}; color: #D9D9D9; text-shadow: 1px 1px #000000; width: 70px" >
                {{ color.color }}  ${{ color.price }}
            </a>
            <img src="{{ color.image }}" style="height: 50px; width: 60px;">
        </li>
    {% endfor %}
</ul>
```

### ecommerce > urls.py -

```python
urlpatterns = [
    path('ajaxcolor/', home.ajaxcolor, name='ajaxcolor'),
]
```


# 3. Product Details Page Intregrate <a href="" name="pro_intregrate"> - </a>

### home > templates > product_detail.html -

```django
<div class="section">
    <!-- container -->
    <div class="container">
        <!-- row -->
        <div class="row">
            <!--  Product Details -->
            <div class="product product-details clearfix">
                <div class="col-md-6">
                    <div id="product-main-view">

                        {% if variant.image_id > 0 %}
                        <div class="product-view">
                            <img src="{{ variant.image }}" style="height: 580px" alt="">
                        </div>
                        {% else %}
                        <div class="product-view">
                            <img src="{{ product.image.url }}" style="height: 580px" alt="">
                        </div>
                        {% endif %}

                        {% for image in images %}
                        <div class="product-view">
                            <img src="{{ image.image.url }}" style="height: 580px" alt="">
                        </div>
                        {% endfor %}
                    </div>

                    <div id="product-view">
                        <div class="product-view">
                            <img src="{{ product.image.url }}" style="height: 150px" alt="">
                        </div>
                        {% for image in images %}
                        <div class="product-view">
                            <img src="{{ image.image.url }}" style="height: 150px" alt="">
                        </div>
                        {% endfor %}
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="product-body">
                        <div class="product-label">
                            <span>New</span>
                            <span class="sale">-20%</span>
                        </div>
                        <h2 class="product-name">{{ product.title }}</h2>

                        <p><strong>Brand:</strong> E-SHOP</p>
                        <p>{{ product.description }}</p>

                        {% if product.variant == 'Size-Color' %}
                        <div class="product-options">
                            <div class="size-option">
                                <form method="POST" id="post-form">
                                    <input type="hidden" name="productid" id="productid" value="{{ product.id }}">
                                    <span class="text-uppercase">Size :</span>
                                    {% csrf_token %}
                                    <select name="size" id="size">
                                        {% for size in sizes %}
                                        <option {% if variant.size_id == size.size_id %} selected {% endif %}
                                            value="{{ size.size_id }}">
                                            {{ size.size.name }}</option>
                                        {% endfor %}
                                    </select>
                                </form>
                            </div>

                            <form method="post" action="?q=selectvariant" id="post-color">
                                {% csrf_token %}
                                <div id="appendHere">
                                    <input type="hidden" name="size" id="size" value="{{ size_id }}">
                                    <ul class="color-option">
                                        <li><span class="text-uppercase">Color:</span></li>
                                        {% for color in colors %}
                                        <input type="radio" {% if variant.id == color.id %} checked {% endif %}
                                            name="variantid" id="variantid" value="{{ color.id }}"
                                            onchange="this.form.submit();">
                                        <li {% if variant.id == color.id %} class="active" {% endif %}>
                                            <a
                                                style="background-color:{{ color.color.code }}; color: #D9D9D9; text-shadow: 1px 1px #000000; width: 90px">
                                                {{ color.price }} {{ color.color }}
                                            </a>
                                            <img src="{{ color.image }}" style="height: 50px; width: 50px;">
                                        </li>
                                        {% endfor %}
                                    </ul>
                                </div>
                            </form>
                        </div>

                        {% elif product.variant == 'Size' %}
                        <div class="product-options">
                            <form method="post" action="?q=selectvariant" id="post-color">
                                {% csrf_token %}
                                <div id="appendHere">
                                    <input type="hidden" name="size" id="size" value="{{ size_id }}">
                                    <ul class="color-option">
                                        <li><span class="text-uppercase">Size:</span></li>
                                        {% for size in sizes %}
                                        <input type="radio" {% if variant.id == size.id %} checked {% endif %}
                                            name="variantid" id="variantid" value="{{ size.id }}"
                                            onchange="this.form.submit();">
                                        <li {% if variant.id == size.id %} class="active" {% endif %}>
                                            <a style=" color: #204d74;  width: 200px">
                                                <div>
                                                    <b>{{ size.size }}</b>
                                                </div>
                                                <div>
                                                    ${{ size.price }}
                                                </div>
                                            </a>
                                            <br>
                                            <br>
                                        </li>
                                        {% endfor %}
                                    </ul>
                                </div>
                            </form>
                        </div>

                        {% elif product.variant == 'Color' %}
                        <div class="product-options">
                            <form method="post" action="?q=selectvariant" id="post-color">
                                {% csrf_token %}
                                <div id="appendHere">
                                    <input type="hidden" name="size" id="size" value="{{ size_id }}">
                                    <ul class="color-option">
                                        <li><span class="text-uppercase">Color:</span></li>
                                        {% for color in colors %}
                                        <input type="radio" {% if variant.id == color.id %} checked {% endif %}
                                            name="variantid" id="variantid" value="{{ color.id }}"
                                            onchange="this.form.submit();">
                                        <li {% if variant.id == color.id %} class="active" {% endif %}>
                                            <a
                                                style="background-color:{{ color.color.code }}; color: #D9D9D9; text-shadow: 1px 1px #000000; width: 90px">
                                                {{ color.price }}  {{ color.color }}
                                            </a>
                                            <img src="{{ color.image }}" style="height: 50px; width: 50px;">
                                        </li>
                                        {% endfor %}
                                    </ul>
                                </div>
                            </form>
                        </div>

                        {% endif %}

                        {% if  product.variant != 'None'   %}
                        <div class="product-btns">
                            <form action="/order/addtoshopcart/{{ product.id }}" method="post" id="addchart-form">
                                {% csrf_token %}
                                <input type="hidden" name="variantid" id="variantid" value="{{ variant.id }}">
                                <div id="SelectedProduct">
                                    <p><strong>Availability:</strong>
                                        {% if variant.quantity > 0  %}
                                        In Stock
                                        {% else %}
                                        Out of Stock
                                        {% endif %}
                                    </p>
                                    <p><strong>Selected :</strong>
                                        Size : {{ variant.size }} Color : {{ variant.color }}
                                    </p>
                                    <h3 class="product-price">${{ variant.price}}</h3>
                                    <div class="qty-input">
                                        <span class="text-uppercase">QTY: </span>
                                        <input class="input" name="quantity" type="number" value="1" min="1"
                                            max="{{ variant.quantity }}">
                                        <button type="submit" {% if variant.quantity < 1  %} disabled {% endif %}
                                            class="primary-btn add-to-cart">
                                            <i class="fa fa-shopping-cart"></i> Add to Cart
                                        </button>
                                    </div>
                                </div>
                            </form>

                            {% else %}

                            <form action="/order/addtoshopcart/{{ product.id }}" method="post" id="addchart-form">
                                {% csrf_token %}
                                <div id="SelectedProduct">
                                    <p><strong>Availability:</strong>
                                        {% if product.amount > 0  %}
                                        In Stock
                                        {% else %}
                                        Out of Stock
                                        {% endif %}</p>
                                    <h3 class="product-price">${{ product.price }}</h3>
                                    <div class="qty-input">
                                        <span class="text-uppercase">QTY: </span>
                                        <input class="input" name="quantity" type="number" value="1" min="1"
                                            max="{{ product.amount }}">
                                        <button type="submit" {% if product.amount < 1  %} disabled {% endif %}
                                            class="primary-btn add-to-cart">
                                            <i class="fa fa-shopping-cart"></i> Add to Cart
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>

                        {% endif %}
                        <div class="pull-right">
                            <button class="main-btn icon-btn"><i class="fa fa-heart"></i></button>
                            <button class="main-btn icon-btn"><i class="fa fa-exchange"></i></button>
                            <button class="main-btn icon-btn"><i class="fa fa-share-alt"></i></button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /Product Details -->
            <div class="col-md-12">
                <div class="product-tab">
                    <ul class="tab-nav">
                        <li class="active"><a data-toggle="tab" href="#tab1">Details</a></li>
                        <li><a data-toggle="tab" href="#tab2">Reviews ( {{ product.countreview }})</a></li>
                    </ul>
                    <div class="tab-content">
                        <div id="tab1" class="tab-pane fade in active">
                            <p>{{ product.details|safe }}</p>
                        </div>
                        <div id="tab2" class="tab-pane fade in">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- /row -->
    </div>
    <!-- /container -->
</div>

{% block scripts %}
<script>
    $(document).on('change', '#post-form', function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '{% url "ajaxcolor" %}',
            data: {
                productid: $('#productid').val(),
                size: $('#size').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            data_type: 'html',
            success: function (data) {
                console.log("success");
                $('#appendHere').html(data.rendered_table);
            },
            error: function (data) {
                alert("Got an error dude " + data);
            }
        });
    });
</script>
{% endblock %}

```

# 4. Order Page Intregrate <a href="" name="ord_intregrate"> - </a>

### order > views.py -

```python
from product.models import Variants

def addtoshopcart(request, id):
product = Product.objects.get(pk=id)

if product.variant != 'None':
    variantid = request.POST.get('variantid')
    checkinvariant = ShopCart.objects.filter(variant_id=variantid, user_id=current_user.id)
    if checkinvariant:
        control = 1
    else:
        control = 0
else:
    checkproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id)
    if checkinproduct:
        control = 1
    else:
        control = 0

if request.method == 'POST':
    form = ShopCartForm(request.POST)
    if form.is_valid():
        if control == 1:
            if product.variant == 'None':
                data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            else:
                data = ShopCart.objects.get(product_id=id, variant_id=variantid, user_id=current_user.id)
            data.quantity += form.cleaned_data['quantity']
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.variant_id = variantid
            data.quantity = form.cleaned_data['quantity']
            data.save()
    return HttpResponseRedirect(url)

else:
    if control == 1:
        data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
        data.quantity += 1
        data.save()
    else:
        data = ShopCart()
        data.user_id = current_user.id
        data.product_id = id
        data.quantity = 1
        data.variant_id = None
        data.save()
    return HttpResponseRedirect(url)

def shopcart(request):
total = 0
for shop in shopcart:
    if shop.product.variant == 'None':
        total += shop.product.price * shop.quantity
    else:
        total += shop.variant.price * shop.quantity

return render(request, 'shopcart_product.html', context)


def orderproduct(request):
category = Category.objects.all()
current_user = request.user
shopcart = ShopCart.objects.filter(user_id=current_user.id)
total = 0
for shop in shopcart:
    if shop.product.variant == 'None':
        total += shop.product.price * shop.quantity
    else:
        total += shop.variant.price * shop.quantity

if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
        data = Order()
        data.first_name = form.cleaned_data['first_name']
        data.last_name = form.cleaned_data['last_name']
        data.address = form.cleaned_data['address']
        data.city = form.cleaned_data['city']
        data.phone = form.cleaned_data['phone']
        data.user_id = current_user.id
        data.total = total
        data.ip = request.META.get('REMOTE_ADDR')
        ordercode = get_random_string(5).upper()
        data.code = ordercode
        data.save()

        for rs in shopcart:
            detail = OrderProduct()
            detail.order_id = data.id
            detail.product_id = rs.product_id
            detail.user_id = current_user.id
            detail.quantity = rs.quantity
            if rs.product.variant == 'None':
                detail.price = rs.product.price
            else:
                detail.price = rs.variant.price
            detail.variant_id = rs.variant_id
            detail.amount = rs.amount
            detail.save()

            if  rs.product.variant=='None':
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()
            else:
                variant = Variants.objects.get(id=rs.product_id)
                variant.quantity -= rs.quantity
                variant.save()

        ShopCart.objects.filter(user_id=current_user.id).delete()
        request.session['cart_items'] = 0
        messages.success(request, "Your Order has been completed. Thank you ")
        return render(request, 'Order_Completed.html', {'ordercode': ordercode, 'category': category})
    else:
        messages.warning(request, form.errors)
        return HttpResponseRedirect("/order/orderproduct")

form = OrderForm()
profile = UserProfile.objects.get(user_id=current_user.id)
context = {
    'shopcart': shopcart,
    'category': category,
    'total': total,
    'form': form,
    'profile': profile,
}
return render(request, 'Order_Form.html', context)
```



### order > templates > shopcart_product.html -

```django
{% for cart in shopcart %}
<tr>
    <td class="thumb">
        {% if cart.variant.image_id  > 0 %}
        <img src="{{ cart.variant.image }}" height="50px" alt="">
        {% else %}
        <img src="{{ cart.product.image.url }}" height="50px" alt="">
        {% endif %}
    </td>
    <td class="details">
        <a href="/product/{{ cart.product.id }}/{{ cart.product.slug }}">
            {{ cart.product.title|truncatewords:"5" }} <br>
            {{ cart.variant.size }} / {{ cart.variant.color }}
        </a>
    </td>
    <td class="price text-center">
        <strong>
            {% if cart.product.variant == 'None' %}
                ${{ cart.product.price }}
            {% else %}
                ${{ cart.variant.price }}
            {% endif %}
        </strong>
    </td>
    <td class="qty text-center"><strong>{{cart.quantity}}</strong></td>
    <td class="total text-center">
        <strong class="primary-color">
            {% if cart.product.variant == 'None' %}
                ${{ cart.amount }}
            {% else %}
                ${{ cart.varamount }}
            {% endif %}
        </strong>
    </td>
    <td class="text-right">
        <a href="/order/deleteshopcart/{{ cart.id }}" class="main-btn icon-btn"
        onclick="return confirm('Delete ! Are you sure?')">
            <i class="fa fa-close"></i>
        </a>
    </td>
</tr>
{% endfor %}
```

### order > templates > Order_Form.html -

```django
{% for shop in shopcart %}
<tr>
    <td class="thumb">
        {% if shop.variant.image_id  > 0 %}
            <img src="{{shop.variant.image }}" alt="">
        {% else %}
            <img src="{{shop.product.image.url}}" alt="">
        {% endif %}    
    </td>
    <td class="details">
        <a href="/product/{{ shop.product.id }}/{{ shop.pslug }}">
            {{ shop.product.title|truncatewords:"4" }} <br>
            {{ shop.variant.size }} / {{ shop.variant.color }}
        </a>
    </td>
    <td class="price text-center">
        <strong>
            {% if shop.product.variant == 'None' %}
                ${{ shop.product.price }}
            {% else %}
                ${{ shop.variant.price }}
            {% endif %}
        </strong>
    </td>
    <td class="qty text-center">
        <strong>{{shop.quantity}}</strong>
    </td>
    <td class="total text-center">
        <strong class="primary-color">
            {% if shopshop.product.variant == 'None' %}
                ${{ shop.amount }}
            {% else %}
                ${{ shop.varamount }}
            {% endif %}
        </strong>
    </td>
</tr>
{% endfor %}
```

# 5. User Page Intregrate <a href="" name="use_intregrate"> - </a>

### user > templates > user_order_detail.html -

```django
{% for orderitem in orderitems %}
<tr>
    <td class="text-left">
        <a href="/product/{{ orderitem.product_id }}/{{ orderitem.product.slug }}">

            {% if orderitem.variant.image_id > 0 %}
            <img src="{{orderitem.variant.image }}" alt="" style="height: 50px">
            {% else %}
            <img src="{{orderitem.product.image.url}}" alt="" style="height: 50px;">
            {% endif %}
                                                
        </a>
    </td>
    <td class="text-left">
        {{ orderitem.product.title|truncatewords:"5"}} <br>
        {{ orderitem.variant.size }} / {{ orderitem.variant.color }}
    </td>
</tr>{% endfor %}
```


# 28. Custom Templates Tags <a href="" name="tags"> - </a>

### home > Create Folder & Files -


- > templatetags
    - > __init__.
    - > ecommercetags.py

### home > templatetags > ecommercetags.py -

```python
from django import template
from order.models import ShopCart
from product.models import Category

register = template.Library()


@register.simple_tag
def categorylist():
    return Category.objects.all()

@register.simple_tag
def shopcartcount(userid):
    count = ShopCart.objects.filter(user_id=userid).count()
    return count

@register.simple_tag
def totalcount(userid):
    shopcart = ShopCart.objects.filter(user_id=userid)
    total = 0
    for shop in shopcart:
        if shop.product.variant == 'None':
            total += shop.product.price * shop.quantity
        else:
            total += shop.variant.price * shop.quantity
    return total
```

### home > templates > sidebar.html -

```django
{% load ecommercetags %}

{% categorylist as category %}

<ul class="category-list">
{% recursetree category %}
<li class="dropdown side-dropdown">
    <a href="/category/{{ node.id }}/{{ node.sluclass="dropdown-toggle"
        {% if not node.is_leaf_node %} data-toggle="droparia-expanded="true"
        {% endif %}>{{ node.title }}
    </a>
    <div class="custom-menu">
        <div class="row">
            <div class="col-md-4">
                {% if not node.is_leaf_node %}
                <ul class="list-links">
                    <li>
                        <h3 class="list-links-title">{{ node.ti</h3>
                    </li>
                    <li>
                        <a href="#">{{ children }}</a>
                    </li>
                </ul>
                {% endif %}
                <hr class="hidden-md hidden-lg">
            </div>
        </div>
    </div>
</li>
{% endrecursetree %}
</ul>
```

### home > templates > header.html -

```django
{% load ecommercetags %}

<select name="catid" class="input search-categories">
<option value="0">All Categories</option>

{% categorylist as category %}

{% recursetree category %}
    {% if node.is_leaf_node %}
        <option value="{{ node.id }}">{{ node.title }}</option>
    {% endif %}
    {% if not node.is_leaf_node %}
        <optgroup label="{{ node.title }}">{{ children }}</optgroup>
    {% endif %}
{% endrecursetree %}</select>


<!-- Cart -->
<li class="header-cart dropdown default-dropdown">
    <a href="/shopcart/">
        <div class="header-btns-icon">
            <i class="fa fa-shopping-cart"></i>
            {% shopcartcount user.id as count %}
            <span class="qty">{{ count }}</span>
        </div>
        <strong class="text-uppercase">My Cart:</strong>
        <br>
        {% totalcount user.id as total %}
        <span>{{ total }}$</span>
    </a>
</li>
<!-- /Cart -->
```