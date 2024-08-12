from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import User, Expense, ExpenseSplit
from .serializers import UserSerializer, ExpenseSerializer, ExpenseSplitSerializer
import os
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseSplitViewSet(viewsets.ModelViewSet):
    queryset = ExpenseSplit.objects.all()
    serializer_class = ExpenseSplitSerializer

class BalanceSheetView(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        balance_sheet = {}
        for user in users:
            expenses = user.expenses.all()
            balance_sheet[user.name] = {
                'total_expenses': sum(expense.amount for expense in expenses),
                'individual_expenses': [
                    {
                        'description': expense.description,
                        'amount': expense.amount,
                        'date': expense.date
                    }
                    for expense in expenses
                ]
            }
        return JsonResponse(balance_sheet)

def generate_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return result

class DownloadBalanceSheetView(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        balance_sheet = {}
        for user in users:
            expenses = user.expenses.all()
            balance_sheet[user.name] = {
                'total_expenses': sum(expense.amount for expense in expenses),
                'individual_expenses': [
                    {
                        'description': expense.description,
                        'amount': expense.amount,
                        'date': expense.date
                    }
                    for expense in expenses
                ]
            }
        context = {'balance_sheet': balance_sheet}
        return generate_pdf('balance_sheet_template.html', context)
    
    # expenses/views.py

def root_view(request):
    return HttpResponse("Hello, this is the root view.")

