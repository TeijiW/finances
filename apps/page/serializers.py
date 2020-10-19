from rest_framework import serializers
from apps.page.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            "name",
            "description",
            "user",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
