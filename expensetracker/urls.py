from django.urls import path
from . import views

urlpatterns = [

    path('income-sources/', views.IncomeSourceListCreateView.as_view(), name='income-source-list'),
    path('income-sources/<int:pk>/', views.IncomeSourceDetailView.as_view(), name='income-source-detail'),
    path('expenses/', views.ExpenseListCreateView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense-detail'),
    path('transactions/', views.TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/summary/', views.TransactionSummaryView.as_view(), name='transaction-summary'),
]