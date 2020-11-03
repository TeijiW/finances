from django.shortcuts import render
from django.views.generic import View

from apps.site.forms import ExpenseForm, BudgetForm
from apps.page.models import Page


# https://docs.djangoproject.com/pt-br/3.1/topics/class-based-views/generic-display/

# def form_handling()


class Home(View):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        if "budget_form" not in kwargs:
            kwargs["budget_form"] = BudgetForm()
        if "expense_form" not in kwargs:
            kwargs["expense_form"] = ExpenseForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    # def post(self, request, *args, **kwargs):
    #     context = {}
    #
    #     if "expense" in request.POST:
    #         form = ExpenseForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             context["expense_form"] = form
    #     elif "budget" in request.POST:
    #         form = BudgetForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             context["budget_form"] = form
    #
    #     return render(request, self.template_name, self.get_context_data(**context))


# def test(request):
#     print(ExpenseForm)
#     if request.method == "POST":
#
#         if "expense" in request.POST:
#             form = ExpenseForm(request.POST)
#         elif "budget" in request.POST:
#             form = ExpenseForm(request.POST)
#         if form.is_valid():
#             print("Is valid")
#             new_expense = form.save(commit=False)
#             page = Page.objects.get(pk=2)
#             new_expense.page = page
#             new_expense.save()
#
#             # return HttpResponseRedirect(reverse("list-view"))
#
#     context = {"budget_form": BudgetForm(), "expense_form": ExpenseForm()}
#     return render(request, "test.html", context)
