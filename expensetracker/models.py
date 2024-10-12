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
