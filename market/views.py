from .models import Product
from django.shortcuts import render
from .forms import UploadFileForm,HowMatchProducts


from . parser import parse_all_info_on_wallmart
from .selen import pick_products

def products(request):
    if "text" in request.POST and "text1" in request.POST:
        HowMatchProducts(request.POST)
        sum_product = request.POST['text']
        id_product = request.POST['text1']
        pick_products(int(sum_product),id_product)
    if "file" in request.FILES:
        UploadFileForm(request.POST, request.FILES)
        file_with_id_products(request.FILES['file'])

    return render(request, 'market/site_page.html', {'products': Product.objects.all()})


def file_with_id_products(file_with_id):
        for id in file_with_id:
            product_id = (id.rstrip()).decode("utf-8")
            parse_all_info_on_wallmart(product_id)






