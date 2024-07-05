# in_house/views.py
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Gullak Expense Tracker!")
