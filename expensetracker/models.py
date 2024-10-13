from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator

class IncomeSource(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="income_sources")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="expanses")
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.category} - {self.user.username}"

class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="transactions")
    income_source = models.ForeignKey(IncomeSource, on_delete=models.SET_NULL, null=True, blank=True)
    expenses = models.ForeignKey(Expense, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators = [MinValueValidator(0.01)])
    transaction_date = models.DateField()
    description = models.TextField(blank=True)

    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.type} - {self.amount} - {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_user_balance()

    def update_user_balance(self):
        if self.type == 'INCOME':
            self.user.current_balance += self.amount
        else:
            self.user.current_balance -= self.amount
        self.user.save()
