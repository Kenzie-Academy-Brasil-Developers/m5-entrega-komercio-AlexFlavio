from rest_framework.test import APITestCase
import ipdb

from account.models import Account
from rest_framework.authtoken.models import Token


class AccountViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.register_url = "/api/accounts/"
        cls.login_url = "/api/login/"
        cls.update_url = "/api/accounts/"

        cls.seller_data = {
            "password": "senha54321",
            "username": "Seller",
            "first_name": "José",
            "last_name": "Roberto",
            "is_seller": True,
        }
        cls.common_data = {
            "password": "senha54321",
            "username": "Common",
            "first_name": "Miguel",
            "last_name": "Garza",
            "is_seller": False,
        }
        cls.seller_login_data = {
            "password": "senha54321",
            "username": "Seller",
        }
        cls.common_login_data = {
            "password": "senha54321",
            "username": "Common",
        }
        ...

    def test_create_seller_account(self):

        response = self.client.post(self.register_url, self.seller_data)
        expectd_status_code = 201
        result_status_code = response.status_code

        self.assertEqual(expectd_status_code, result_status_code)

        ...

    def test_create_common_account(self):

        response = self.client.post(self.register_url, self.common_data)
        expectd_status_code = 201
        result_status_code = response.status_code

        self.assertEqual(expectd_status_code, result_status_code)
        ...

    def test_create_seller_account_invalid_keys(self):
        user_data = {}

        response = self.client.post(self.register_url, user_data)
        expectd_status_code = 400
        result_status_code = response.status_code

        self.assertEqual(expectd_status_code, result_status_code)
        ...

    def test_create_common_account_invalid_keys(self):
        user_data = {}

        response = self.client.post(self.register_url, user_data)
        expectd_status_code = 400
        result_status_code = response.status_code

        self.assertEqual(expectd_status_code, result_status_code)
        ...

    def test_login_common_account(self):

        response = self.client.post(self.register_url, self.common_data)

        teste = self.client.post(self.login_url, self.common_login_data)
        ipdb.set_trace()
        expectd_status_code = 200
        result_status_code = response.status_code

        self.assertEqual(expectd_status_code, result_status_code)
        self.assertIn("token", response.data)

        ...

    def test_login_seller_account(self):
        response = self.client.post(self.register_url, self.seller_data)
        response = self.client.post(self.login_url, self.seller_login_data)

        expectd_status_code = 200
        result_status_code = response.status_code

        ipdb.set_trace()
        print()
        print(response.json())
        self.assertEqual(expectd_status_code, result_status_code)
        self.assertIn("token", response.data)
        ...

    def test_account_owner_update(self):
        account_owner = Account.objects.create_user(**self.seller_data)
        token = Token.objects.create(account=account_owner)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.patch(
            f"{self.update_url}{account_owner.id}/", data={"first_name": "Sancho"}
        )
        expectd_status_code = 200
        result_status_code = response.status_code
        self.assertEqual(expectd_status_code, result_status_code)
        ...

    def test_super_user_soft_delet_account(self):
        
        ...

    def test_super_user_reactive_account(self):
        ...

    def test_list_users(self):
        ...
