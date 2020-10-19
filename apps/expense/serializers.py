from rest_framework import serializers
from apps.expense.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "name",
            "description",
            "value",
            "status",
            "page",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
