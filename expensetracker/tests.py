from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import IncomeSource, Expense, Transaction

class ExpenseTrackerTestCase(TestCase):

    def setUp(self):
        """Create a user and set up initial data for tests."""
        self.user = get_user_model().objects.create_user(
            email="testuser@mail.com",
            username="testuser",
            password="password123"
        )
        self.income_source = IncomeSource.objects.create(
            user=self.user,
            name="Salary",
            description="Monthly salary"
        )
        self.expense = Expense.objects.create(
            user=self.user,
            name="Rent",
            category="Housing"
        )

    def test_income_source_creation(self):
        """Test creating an income source."""
        self.assertEqual(self.income_source.user, self.user)
        self.assertEqual(self.income_source.name, "Salary")
        self.assertEqual(self.income_source.description, "Monthly salary")
        self.assertEqual(str(self.income_source), "Salary - testuser")

    def test_expense_creation(self):
        """Test creating an expense."""
        self.assertEqual(self.expense.user, self.user)
        self.assertEqual(self.expense.name, "Rent")
        self.assertEqual(self.expense.category, "Housing")
        self.assertEqual(str(self.expense), "Rent - Housing - testuser")

    def test_transaction_creation_income(self):
        """Test creating a transaction of type INCOME."""
        transaction = Transaction.objects.create(
            user=self.user,
            income_source=self.income_source,
            amount=1000.00,
            transaction_date="2024-01-01",
            description="Monthly Salary",
            type="INCOME"
        )
        self.assertEqual(transaction.type, "INCOME")
        self.assertEqual(transaction.amount, 1000.00)
        self.assertEqual(transaction.user.current_balance, 1000.00)
        self.assertEqual(str(transaction), "INCOME - 1000.00 - testuser")

    def test_transaction_creation_expense(self):
        """Test creating a transaction of type EXPENSE."""
        transaction = Transaction.objects.create(
            user=self.user,
            expenses=self.expense,
            amount=200.00,
            transaction_date="2024-01-01",
            description="Monthly Rent",
            type="EXPENSE"
        )
        self.assertEqual(transaction.type, "EXPENSE")
        self.assertEqual(transaction.amount, 200.00)
        self.assertEqual(transaction.user.current_balance, -200.00)
        self.assertEqual(str(transaction), "EXPENSE - 200.00 - testuser")

    def test_user_balance_update_income(self):
        """Test that the user's balance updates correctly after income transaction."""
        transaction = Transaction.objects.create
