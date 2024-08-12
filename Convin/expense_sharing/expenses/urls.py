from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExpenseViewSet, ExpenseSplitViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'expense-splits', ExpenseSplitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
