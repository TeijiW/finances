from django.db import models
from apps.page.models import Page


class Expense(models.Model):

    EXPENSE_STATUS = (("P", "Paid"), ("NP", "Not Paid"), ("C", "Canceled"))

    name = models.CharField("Name", max_length=120)
    description = models.TextField()
    value = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(max_length=12, choices=EXPENSE_STATUS)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
