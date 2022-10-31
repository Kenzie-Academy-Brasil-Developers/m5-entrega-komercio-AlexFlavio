from django.test import TestCase
import uuid

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from account.models import Account
from product.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...

    def test_id_default(self):
        expected = uuid.uuid4
        result = Product._meta.get_field("id").default
        msg = f'Verifique se a propriedade "default" de id está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_id_primary_key(self):
        expected = True
        result = Product._meta.get_field("id").primary_key
        msg = f'Verifique se a propriedade "primary_key" de id está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_id_editable(self):
        expected = False
        result = Product._meta.get_field("id").editable
        msg = f'Verifique se a propriedade "editable" de id está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_price_max_digits(self):
        expected = 10
        result = Product._meta.get_field("price").max_digits
        msg = f'Verifique se a propriedade "max_digits" de price foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_price_defimal_places(self):
        expected = 2
        result = Product._meta.get_field("price").decimal_places
        msg = f'Verifique se a propriedade "decimal_places" de price foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_is_active_default(self):
        expected = True
        result = Product._meta.get_field("is_active").default
        msg = f'Verifique se a propriedade "default" de is_active foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_is_active_null(self):
        expected = True
        result = Product._meta.get_field("is_active").null
        msg = f'Verifique se a propriedade "null" de is_active foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    ...


class ProductRelationShipTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_data = {
            "username": "usuario1",
            "first_name": "usuario",
            "last_name": "1",
            "is_seller": True,
        }
        cls.product1_data = {
            "description": "Produto de teste N1",
            "price": 199.99,
            "quantity": 10,
        }
        cls.product2_data = {
            "description": "Produto de teste N1",
            "price": 199.99,
            "quantity": 10,
        }

        cls.account = Account.objects.create_user(**cls.account_data)
        ...

    def test_many_to_one_relationship_with_account(self):
        ...
