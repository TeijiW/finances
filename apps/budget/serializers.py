from rest_framework import serializers
from apps.budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = [
            "name",
            "description",
            "value",
            "page",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
