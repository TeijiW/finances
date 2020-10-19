from rest_framework.viewsets import ModelViewSet
from apps.budget.models import Budget
from apps.budget.serializers import BudgetSerializer


class BudgetViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()
    search_fields = ["name", "description"]
    filterset_fields = ["name", "description", "status"]
