import json
from django.shortcuts import render
from django.contrib import messages
from .models import Setting, ContactForm, ContactMessage, FAQ
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from product.models import Category, Product, Images, Comment, CommentForm, Variants
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from order.models import ShopCart
from ecommerce import settings
from django.urls import reverse
from .forms import SearchForm


def index(request):
    setting = Setting.objects.get(pk=1)
    product_slider = Product.objects.all()
    product_slider = Product.objects.filter(featured=True)[:3]
    product_latest = Product.objects.filter(featured=False).order_by('-id')[:4]
    product_pick = Product.objects.filter(featured=False).order_by('?')[:4]
    page = 'home'
    
    context = {
        'setting': setting,
        'page': page,
        'product_slider': product_slider,
        'product_latest': product_latest,
        'product_pick': product_pick,
    }
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting,
    }
    return render(request, 'about.html', context)


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
            messages.success(
                request, "Your message has been sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')
    form = ContactForm
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting,
        'form': form,
    }
    return render(request, 'contact.html', context)


def category(request, id, slug):
    category_data = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'products': products,
        'category_data': category_data,
    }
    return render(request, 'category.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=catid)
            context = {
                'products': products,
                'query': query,
            }
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')


def searchAuto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for product in products:
            product_json = {}
            product_json = product.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, id, slug):
    query = request.GET.get('q')
    product = Product.objects.get(id=id)
    product_random = Product.objects.filter(featured=False).order_by('?')[:4]
    comments = Comment.objects.filter(product_id=id, status='True')
    images = Images.objects.filter(product_id=id)
    context = {
        'product': product,
        'images': images,
        'product_random': product_random,
        'comments': comments,
    }

    if product.variant != "None":
        if request.method == 'POST':
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id)
            colors = Variants.objects.filter(
                product_id=id, size_id=variant.size_id)
            sizes = Variants.objects.raw(
                'SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
            query += variant.title+' Size:' + \
                str(variant.size) + ' Color:' + str(variant.color)
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
        data = {'rendered_table': render_to_string(
            'color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)



def faq(request):
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")

    context = {
        'faq': faq,
    }
    return render(request, 'faq.html', context)
