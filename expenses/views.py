from rest_framework import status, views
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
import openai
from django.conf import settings


class CategorizeExpenseView(views.APIView):
    def post(self, request, *args, **kwargs):
        transactions = request.data.get("transactions", [])
        categorized_transactions = self.categorize_expenses(transactions)
        serializer = TransactionSerializer(data=categorized_transactions, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def categorize_expenses(self, transactions):
        openai.api_key = settings.OPENAI_API_KEY
        prompt = "Categorize the following transactions:\\n"
        for transaction in transactions:
            prompt += f"Date: {transaction['transaction_date']}, Amount: {transaction['amount']}, Description: {transaction['description']}\\n"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        categorized_transactions = self.parse_response(
            response.choices[0].text, transactions
        )
        return categorized_transactions

    def parse_response(self, response, transactions):
        lines = response.strip().split("\\n")
        categories = ["food", "travel", "shopping", "entertainment", "other"]

        categorized_transactions = []
        for line, transaction in zip(lines, transactions):
            category = "other"
            for c in categories:
                if c in line.lower():
                    category = c
                    break
            transaction["category"] = category
            categorized_transactions.append(transaction)

        return categorized_transactions
