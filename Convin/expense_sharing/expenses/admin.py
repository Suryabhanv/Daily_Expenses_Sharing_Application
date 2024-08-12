from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Expense, ExpenseSplit

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(ExpenseSplit)
