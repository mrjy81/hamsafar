from django.test import TestCase
from .models import Client, Driver, Phones


class TestAccount(TestCase):
    def setUp(self):
        # Setup run before every test method.
        phone = Phones.objects.create(phone='9104890853')
        Driver.objects.create(user__username='driver1',
                              phone=phone,  password='123')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_create_driver(self):
        pass
