from django.test import TestCase
from django.core.management import call_command
from io import StringIO
import json
from api.product_data import products

from graphene_django.utils.testing import GraphQLTestCase


class APITestCase(TestCase):
    
    def test_importdata_command(self):
        " Test importdata command."

        out = StringIO()
        call_command('importdata', stdout=out)
        self.assertIn('uccessfully imported products data', out.getvalue())
        


class DataTestCase(GraphQLTestCase):

    def setUp(self):
        self.GRAPHQL_URL = '/graphql'
        call_command('importdata')

    def test_some_query(self):

        response = self.query(
            '''
            query {
                allProducts {
                    id
                    name
                }
            }
            ''',
        )

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)


    def test_json_data(self):

        response = self.query(
            '''
            query {
                allProducts {
                    name
                    description
                    sku
                    price
                    image
                    
                }
            }
            ''',
        )
        content = json.loads(response.content)
        
        # This validates if the allProducts object is not empty
        self.assertNotEquals(content['data']['allProducts'], [])

