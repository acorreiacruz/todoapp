from rest_framework.test import APITestCase
from .test_api_mixin import TestAPIMixin


class TestTodoAPI(APITestCase, TestAPIMixin):
    ...
