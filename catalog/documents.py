import json
import bson

from django.conf import settings

from mongoengine import connect
from mongoengine import Document
from mongoengine import fields


mongo_conn = settings.MONGO_CONNECTION_PARAMS


connect(
    db=mongo_conn['DB'],
    alias='default',
    host=mongo_conn['HOST'],
    port=mongo_conn['PORT'],
    username=mongo_conn['USERNAME'],
    password=mongo_conn['PASSWORD'],
    retryWrites=False
)


class ProductDocument(Document):
    '''
    "id": 1,
    "title": "Pantalla LCD Sony 46 Pulgadas HD KDL-46V5100 | Elektra Online",
    "description": "Encuentra una amplia variedad de artículos directos a la puerta de tu hogar en Elektra Online",
    "url": "https://www.elektra.com.mx/Pantalla-LCD-Sony-46-Pulgadas-HD-KDL-46V5100-13775",
    "price": "$25,499.00",
    "image": "https://elektraqapre.vteximg.com.br/arquivos/ids/157062-292-292/13775.jpg?v=636568020121500000",
    "auctions": {},
    "specifications": []
    '''
    prod_id = fields.IntField()
    title = fields.StringField()
    description = fields.StringField()
    url = fields.URLField()
    price = fields.StringField()
    image = fields.URLField()
    auctions = fields.DictField()
    offers = fields.ListField(fields.ListField())
    specifications = fields.ListField()

    def __init__(self, *args, **kwargs):
        try:
            id = kwargs.pop('id')
            kwargs['prod_id'] = int(id)
        except (TypeError,) as exc:
            print(exc)
        super().__init__(*args, **kwargs)

    def to_json(self):
        product = bson.json_util.dumps(self.to_mongo())
        product = json.loads(product)
        return product
