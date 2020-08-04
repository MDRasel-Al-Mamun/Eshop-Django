"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Other App Import
from home import views as home
from order import views as order
from user import views as user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('tinymce/', include('tinymce.urls')),


    # Home App Urls
    path('about/', home.about, name='about'),
    path('contact/', home.contact, name='contact'),
    path('category/<int:id>/<slug:slug>', home.category, name='category'),
    path('search/', home.search, name='search'),
    path('search_auto/', home.searchAuto, name='search_auto'),
    path('product/<int:id>/<slug:slug>', home.product_detail, name='product'),
    path('faq/', home.faq, name='faq'),
    path('ajaxcolor/', home.ajaxcolor, name='ajaxcolor'),

    # Order App Urls
    path('shopcart/', order.shopcart, name='shopcart'),

    # User App Urls
    path('login/', user.login_form, name='login'),
    path('signup/', user.signupUser, name='signup'),
    path('logout/', user.logoutUser, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
