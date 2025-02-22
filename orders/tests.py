from django.test import TestCase
from .models import Order

class OrderTestCase(TestCase):
    def test_order_creation(self):
        order = Order.objects.create(
            table_number=5,
            items=[{'name': 'Кофе', 'price': 200}],
            status='pending'
        )
        self.assertEqual(order.total_price, 200)
