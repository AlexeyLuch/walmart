import sqlite3
import requests
from lxml import html
from .models import Product


def parse_all_info_on_wallmart(product_id):
    get_link_to_product = requests.get("https://www.walmart.com/ip/%s" % (product_id))
    to_dom_constraction = html.fromstring(get_link_to_product.content)
    try:
        description = to_dom_constraction.xpath(
            '//*[@class="prod-ProductHighlights-description xs-margin-top"]//text()')
        description = (".".join(description)).replace('"', '').replace('\'', '')
    except:
        description = "without"
    url = ("https://www.walmart.com/ip/" + product_id)
    title = (to_dom_constraction.xpath("//div[@class='hf-Bot']/h1[@class='prod-ProductTitle font-normal']/text()")[0]).replace('"', '')
    price = to_dom_constraction.xpath("//*[@id='price']//span[@class='visuallyhidden']/text()")[0]
    rating_views = to_dom_constraction.xpath('//*[@class="stars-container"]/@aria-label')[0]
    try:
        delivery = to_dom_constraction.xpath('//div[@class="fulfillment-shipping-text"]/span/text()')[0]
    except:
        delivery = "without information"
    brand = to_dom_constraction.xpath('//div/a[@class="prod-brandName"]/span/text()')[0]
    amount = len(to_dom_constraction.xpath(
        '//*[@class="prod-ProductCTA primaryProductCTA-marker"]//select[@class="field-input field-input--secondary"]/option/text()'))
    try:
        in_stock = to_dom_constraction.xpath('//*[@class="display-block-xs font-bold"]/text()')[0]

    except:
        in_stock = "in stoke"
    try:
        category = to_dom_constraction.xpath('//li[@class="breadcrumb active"]/a/span/span/text()')[0]
        print(category)
    except:
        category = "without category"
        pass

    save_product = Product(id_product=product_id,title=title,in_stock=in_stock,price=price,url=url,description=description,
                category=category,rating_reviews=rating_views,brand=brand,amount=amount,delivery_price=delivery)
    save_product.save()
