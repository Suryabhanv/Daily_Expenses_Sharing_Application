from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import User, Expense, ExpenseSplit

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(email='test@example.com', name='Test User', mobile_number='1234567890')

    def test_user_creation(self):
        user = User.objects.get(email='test@example.com')
        self.assertEqual(user.name, 'Test User')

class ExpenseModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(email='test@example.com', name='Test User', mobile_number='1234567890')
        Expense.objects.create(user=user, description='Test Expense', amount=100.00, split_method='equal')

    def test_expense_creation(self):
        expense = Expense.objects.get(description='Test Expense')
        self.assertEqual(expense.amount, 100.00)
