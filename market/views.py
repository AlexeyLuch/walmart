from .models import Product
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

import sqlite3
import requests
from lxml import html

def products(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/market/')
    else:
        form = UploadFileForm()
    return render(request, 'market/site_page.html', {'products': Product.objects.all()})


def handle_uploaded_file(f):
    with open('media/tokens.txt', 'wb+') as destination:
        for chunk in f.chunks():

            product_id = (chunk.rstrip()).decode("utf-8")

            def made_link_to_parse():
                get_link_to_product = requests.get("https://www.walmart.com/search/?query=%s" % (product_id))
                to_dom_constraction = html.fromstring(get_link_to_product.content)
                content = to_dom_constraction.xpath('//*[contains(@class, "search-result-productimage")]/@href')
                print("https://www.walmart.com" + content[0])
                description = to_dom_constraction.xpath('//*[@class="prod-desc-priceUI-1"]/li/text()')
                description = (".".join(description)).replace('"', '').replace('\'', '')

                c = "https://www.walmart.com" + content[0]
                return (c,description)

            def parse_all_info():

                url = made_link_to_parse()
                description = url[1]
                link_to_product_info = requests.get(url[0])
                to_dom_constraction = html.fromstring(link_to_product_info.content)
                title = (
                to_dom_constraction.xpath("//div[@class='hf-Bot']/h1[@class='prod-ProductTitle font-normal']/text()")[0])
                title = title.replace('"', '')
                price = to_dom_constraction.xpath("//*[@id='price']//span[@class='visuallyhidden']/text()")[0]
                rating_views = to_dom_constraction.xpath('//*[@class="stars-container"]/@aria-label')[0]
                in_stock = True
                try:
                    id = to_dom_constraction.xpath(
                        '//div[@class="valign-middle secondary-info-margin-right copy-mini display-inline-block wm-item-number"]')[ 0]
                    id_product_walmart = ((id.text).split())[-1]
                except:
                    id_product_walmart = "without"
                    pass

                try:
                    delivery = to_dom_constraction.xpath('//div[@class="fulfillment-shipping-text"]/span/text()')[0]
                except:
                    delivery = "without information"
                brand = to_dom_constraction.xpath('//div/a[@class="prod-brandName"]/span/text()')[0]
                amount = len(to_dom_constraction.xpath(
                    '//*[@class="prod-ProductCTA primaryProductCTA-marker"]//select[@class="field-input field-input--secondary"]/option/text()'))
                try:
                    category = to_dom_constraction.xpath('//li[@class="breadcrumb active"]/a/span/span/text()')[0]
                    print(category)
                except:
                    category = "without category"
                    pass
                db = sqlite3.connect('/home/luch/PycharmProjects/test_walmart/walmart/db.sqlite3')
                cur = db.cursor()
                query = 'INSERT INTO market_product ( "id_product","title" ,"in_stock", "price" ,"url","description","category","rating_reviews","brand","amount","delivery_price" ) ' \
                        'VALUES ( "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s" )' % (
                        id_product_walmart, title,in_stock, price, url[0], description, category, rating_views, brand,
                        amount, delivery)
                cur.execute(query)
                db.commit()

            parse_all_info()


