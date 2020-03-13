from django.views import View

from .models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm,HowMatchProducts

import sqlite3
import requests
from lxml import html


from . parser import parse_all_info
from .selen import pick_products

def products(request):
    if "text" in request.POST and "text1" in request.POST:
        HowMatchProducts(request.POST)
        sum_product = request.POST['text']
        id_product = request.POST['text1']
        pick_products(int(sum_product),id_product)
    if "file" in request.FILES:
        UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['file'])

    return render(request, 'market/site_page.html', {'products': Product.objects.all()})


def handle_uploaded_file(f):
        for chunk in f:
            product_id = (chunk.rstrip()).decode("utf-8")
            parse_all_info(product_id)






