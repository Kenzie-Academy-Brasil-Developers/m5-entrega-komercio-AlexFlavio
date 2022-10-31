from django.test import TestCase
import uuid

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from account.models import Account


class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...

    def test_id_default(self):
        expected = uuid.uuid4
        result = Account._meta.get_field("id").default
        msg = f'Verifique se a propriedade "default" de id está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_id_primary_key(self):
        expected = True
        result = Account._meta.get_field("id").primary_key
        msg = f'Verifique se a propriedade "primary_key" de id está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_id_editable(self):
        expected = False
        result = Account._meta.get_field("id").editable
        msg = f'Verifique se a propriedade "editable" de id está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_username_unique(self):
        expected = True
        result = Account._meta.get_field("username").unique
        msg = f'Verifque se a propriedade "unique" de username está == {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_first_name_max_length(self):
        expected = 50
        result = Account._meta.get_field("first_name").max_length
        msg = f'Verifique se a propriedade "max_length" de first_name foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_last_name_max_length(self):
        expected = 50
        result = Account._meta.get_field("last_name").max_length
        msg = f'Verifique se a propriedade "max_length" de last_name foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    def test_is_seller_default(self):
        expected = False
        result = Account._meta.get_field("is_seller").default
        msg = f'Verifique se a propriedade "default" de last_name foi definida como {expected}'
        self.assertEqual(expected, result, msg)
        ...

    ...
