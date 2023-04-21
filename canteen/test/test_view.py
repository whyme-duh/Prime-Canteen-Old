from multiprocessing.connection import Client
from urllib import response

from django.contrib.auth.models import User
from django.test import Client, TestCase

from canteen.models import *
from canteen.views import *


class TestViewResponse(TestCase):
	def setUp(self):
		self.c = Client()
		
	
	def test_url(self):
		response = self.c.get('/', HTTP_HOST="asdf.com")
		self.assertEqual(response.status_code, 400)
		response = self.c.get('/', HTTP_HOST="127.0.0.1")
		self.assertEqual(response.status_code, 200)

	

