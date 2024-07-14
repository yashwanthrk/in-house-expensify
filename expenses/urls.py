from django.urls import path
from .views import RegisterView, LoginView, CategorizeExpenseView, TransactionListView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("categorize/", CategorizeExpenseView.as_view(), name="categorize"),
    path("transactions/", TransactionListView.as_view(), name="transactions"),
]
