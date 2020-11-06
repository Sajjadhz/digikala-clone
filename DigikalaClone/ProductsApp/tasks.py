import requests, bs4
from .models import Product
from celery import shared_task

def normalize_numbers(string):
    farsi = '۰۱۲۳۴۵۶۷۸۹'
    english = '0123456789'
    number = ''
    for char in string:
        place = farsi.find(char)
        number+=english[place]
    return number

@shared_task
def populate_product():
    url = 'https://www.digikala.com/search/category-mobile-phone/?pageno='
    names = []
    prices = []

    Product.objects.all().delete()

    for page in range(1,4):
        print('page .....{}'.format(page))
        page = requests.get(url + str(page))
        soup = bs4.BeautifulSoup(page.text, 'html.parser')

        html_names = soup.select('div.c-product-box__content--row')
        html_prices = soup.select('div.c-price__value')

        for char in html_names:
            name = char.text.encode('latin1', 'ignore').decode('UTF-8').strip()
            names.append(name)
        for char in html_prices:
            
            price = char.text.strip().split(' ')[0].replace(',','')
            if price == '':
                pass
            else:
                prices.append(int(normalize_numbers(price)))
        print('finish page ....{}'.format(page))

    for i in range(0, len(names)):
        Product.objects.create(name=names[i], price=prices[i])
