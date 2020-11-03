from django import forms
from django.contrib.auth.forms import AuthenticationForm

from apps.budget.models import Budget
from apps.expense.models import Expense


class UserLoginForm(AuthenticationForm):

    input_class = (
        "appearance-none block w-full px-3 py-2 border-2 border-blue-550 "
        "rounded-10 placeholder-blue-550 focus:border-blue-600 focus:outline-none "
        "transition duration-150 ease-in-out sm:text-sm sm:leading-5"
    )

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": input_class,
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": input_class,
            }
        )
    )


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["name", "description", "value", "status", "page"]


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ["name", "description", "value", "page"]
