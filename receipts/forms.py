from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory, Account
from django import forms


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
        ]


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "name",
            "number",
        ]
