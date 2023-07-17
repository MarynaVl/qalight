import json

import requests


class PageBookStoreUsers:
    URL = 'https://demoqa.com'
    END_POINT = '/Account/v1/User'

    def __init__(self):
        self.user = None

    def create_user(self, user_name, password):
        model = {
            "userName": user_name,
            "password": password
        }
        response = requests.post(url=self.URL + self.END_POINT, data=model)
        status = response.status_code
        assert status == 201
        new_user = json.loads(response.content)
        return {'name': new_user.get('username'), 'id': new_user.get('userID')}
