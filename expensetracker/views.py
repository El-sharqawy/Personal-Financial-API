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

class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")


        transactions = Transaction.objects.filter(user=request.user)
        if start_date:
            transactions = transactions.filter(transaction_date__gte=start_date)

        if end_date:
            transactions = transactions.filter(transaction_date__gte=end_date)

        income = transactions.filter(type="INCOME").aggregate(Sum("amount"))["amount__sum"] or 0
        expenses = transactions.filter(type="EXPENSE").aggregate(Sum("amount"))["amount__sum"] or 0

        return Response({
                    'total_income': income,
                    'total_expenses': expenses,
                    'net': income - expenses
                })