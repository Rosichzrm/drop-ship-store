from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from zoneinfo import ZoneInfo



from shop.models import Product, Payment, Order, OrderItem

# Create your tests here.
class TestDataBase(TestCase):
    fixtures = [
        "shop/fixtures/data.json"
    ]

    def setUp(self):
        self.user = User.objects.get(username='root')

    def test_user_exists(self):
        users = User.objects.all()
        users_number = users.count()
        user = users.first()
        self.assertEqual(users_number, 1)
        self.assertEqual(user.username, 'root')
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('123'))

    def test_all_data(self):
        self.assertGreater(Product.objects.all().count(), 0)
        #self.assertGreater(Payment.objects.all().count(), 0)
        #self.assertGreater(Order.objects.all().count(), 0)
        #self.assertGreater(OrderItem.objects.all().count(), 0)


    def find_cart_number(self):
        cart_number = Order.objects.filter(user=self.user, status=Order.STATUS_CART).count()

        return cart_number


    def test_function_get_cart(self):
        pass

        # 1. No carts
        self.assertEqual(self.find_cart_number(), 0)

        # 2. Create cart
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)

        # 3. Get created cart
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)


    def test_cart_order_7_days(self):
        cart = Order.get_cart(self.user)
        cart.creation_time = timezone.datetime(2000, 1, 1, tzinfo=ZoneInfo('UTC'))
        cart.save()
        cart = Order.get_cart(self.user)
        self.assertEqual((timezone.now() - cart.creation_time).days, 0)
