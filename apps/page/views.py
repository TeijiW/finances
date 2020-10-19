from rest_framework.viewsets import ModelViewSet
from apps.page.models import Page
from apps.page.serializers import PageSerializer


class PageViewSet(ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    search_fields = ["name", "description"]
    filterset_fields = ["name", "description"]
