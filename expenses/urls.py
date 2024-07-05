from django.urls import path
from .views import CategorizeExpenseView

urlpatterns = [
    path("categorize/", CategorizeExpenseView.as_view(), name="categorize_expense"),
]
