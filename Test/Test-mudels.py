import unittest
from service.models import Product

class TestProductModel(unittest.TestCase):

    def test_read_product(self):
        product = Product(id=1, name="Test Product", category="Test Category", available=True, price=9.99)
        self.assertEqual(product.id, 1)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.category, "Test Category")
        self.assertTrue(product.available)
        self.assertEqual(product.price, 9.99)

    def test_update_product(self):
        product = Product(id=1, name="Old Name", category="Old Category", available=True, price=5.0)
        product.name = "New Name"
        product.category = "New Category"
        product.available = False
        product.price = 10.0
        self.assertEqual(product.name, "New Name")
        self.assertEqual(product.category, "New Category")
        self.assertFalse(product.available)
        self.assertEqual(product.price, 10.0)
