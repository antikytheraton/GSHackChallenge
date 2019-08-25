import requests


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
        return {'speficifications': response.json()}

    def get_data(self):
        try:
            details = self._get_details()
            variants = self._get_variants()
            specifications = self._get_specifications()
            return {**details, **variants, **specifications}
        except (AttributeError,) as exc:
            return None
