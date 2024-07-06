from django.urls import path
from .views import CategorizeExpenseView, RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("categorize/", CategorizeExpenseView.as_view(), name="categorize_expense"),
]
