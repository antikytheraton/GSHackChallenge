import requests
from random import choice
from datetime import datetime, timedelta


class ProductClient(object):

    BASE_URL_1 = 'https://challenge.ektdevelopers.com/api/catalog_system/pvt/products/'
    BASE_URL_2 = 'https://challenge.ektdevelopers.com/api/catalog_system/pub/products/'

    def __init__(self, productId):
        self.productId = productId

    def _get_details(self):
        url = f'{self.BASE_URL_1}ProductGet/{self.productId}'
        response = requests.get(url)
        response = response.json()
        return {
            'id': response.get('Id', None),
            'title': response.get('Title', None),
            'description': response.get('MetaTagDescription', None),
            'url': f"https://www.elektra.com.mx/{response.get('LinkId', '')}",
        }

    def _get_variants(self):
        url = f'{self.BASE_URL_2}variations/{self.productId}'
        response = requests.get(url)
        response = response.json()
        product = response.get('skus')[0]
        return {
            'price': product.get('bestPriceFormated', None),
            'image': product.get('image', None),
        }

    def _get_specifications(self):
        url = f'{self.BASE_URL_1}{self.productId}/specification'
        response = requests.get(url)
        return {'specifications': response.json()}

    def _get_auctions(self):
        date = datetime.now() + timedelta(days=choice([2, 5, 6, 10]))
        empty = {}
        auction = {
            'date': date,
            'price': None
        }
        options = [empty, auction]
        return {'auctions': choice(options)}

    def get_data(self):
        try:
            details = self._get_details()
            variants = self._get_variants()
            specifications = self._get_specifications()
            auctions = self._get_auctions()
            return {**details, **variants, **auctions, **specifications}
        except (AttributeError,) as exc:
            return None
