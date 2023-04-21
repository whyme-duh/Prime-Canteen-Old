from django.test import TestCase

from canteen.models import *


class TestCategoriesModel(TestCase):

	def setUp(self):
		self.data1 = Category.objects.create(name = 'ritik', slug= 'ritik')

	def test_category_model_entry(self):
		data = self.data1
		self.assertTrue(isinstance(data, Category))


	def test_category_model_return(self):
		data = self.data1
		self.assertEqual(str(data), 'ritik')

class TestFoodModel(TestCase):
	
	def setUp(self):
		Category.objects.create(name="ritik", slug="ritik")
		self.data1 = Food.objects.create(name = 'ritik', slug= 'ritik', price='6', category_id= 1)

	def test_food_model_entry(self):
		data = self.data1
		self.assertTrue(isinstance(data, Food))


	def test_food_model_return(self):
		data = self.data1
		self.assertEqual(str(data), 'ritik')