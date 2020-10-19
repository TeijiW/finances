from rest_framework import viewsets
from apps.expense.models import Expense
from apps.expense.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    search_fields = ["name", "description"]
    filterset_fields = ["name", "description", "status"]
