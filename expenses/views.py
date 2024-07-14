from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, User
from .serializers import TransactionSerializer, UserSerializer
import openai
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

import logging

logger = logging.getLogger(__name__)


class RegisterView(views.APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        logger.debug(f"Login attempt for email: {email}")
        user = authenticate(username=email, password=password)
        if user:
            logger.debug(f"Authentication successful for email: {email}")
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        logger.debug(f"Authentication failed for email: {email}")
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


openai.api_key = settings.OPENAI_API_KEY


class CategorizeExpenseView(views.APIView):
    def post(self, request, *args, **kwargs):
        transactions = request.data.get("transactions", [])
        try:
            categorized_transactions = self.categorize_expenses(transactions)
        except (
            openai.OpenAIError
        ) as e:  # Update the exception handling to the new OpenAIError class
            logger.error(f"Error categorizing expenses: {e}")
            return Response(
                {"error": "Failed to categorize expenses"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        serializer = TransactionSerializer(data=categorized_transactions, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def categorize_expenses(self, transactions):
        prompt_lines = ["Categorize the following transactions:"]
        for transaction in transactions:
            prompt_lines.append(
                f"Date: {transaction['transaction_date']}, Amount: {transaction['amount']}, Description: {transaction['description']}"
            )
        prompt = "\n".join(prompt_lines)

        # Update the OpenAI API call to the new ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Process the response as per the new API response structure
        categorized_transactions = (
            response["choices"][0]["message"]["content"].strip().split("\n")
        )
        return categorized_transactions


class TransactionListView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        transactions = Transaction.objects.filter(user=user).order_by(
            "-transaction_date"
        )
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
