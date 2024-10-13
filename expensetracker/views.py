from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import QuerySet, Sum
from .models import IncomeSource, Expense, Transaction
from users.models import CustomUser
from .serializers import IncomeSourceSerializer, ExpenseSerializer, TransactionSerializer

class IncomeSourceListCreateView(generics.ListCreateAPIView):
    serializer_class = IncomeSourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IncomeSource.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IncomeSourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IncomeSource.objects.filter(user=self.request.user)
