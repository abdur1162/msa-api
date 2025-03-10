from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

class InvoiceDummyDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Public access (remove this if authentication is needed)

    def get(self, request, *args, **kwargs):
        dummy_invoice = {
            "invoice_number": "INV-2025001",
            "invoice_date": "2025-03-07",
            "due_date": "2025-03-21",
            "seller_company_name": "Tech Solutions Pvt Ltd",
            "seller_address": "1234 Tech Park, Bangalore, India",
            "seller_contact": "Johndoe@gmail.com",
            "seller_phone": "98765 43210",
            "seller_tax_id": "GST123456789",
            "buyer_company_name": "Innovate Enterprises",
            "buyer_address": "5678 Business Hub, Mumbai, India",
            "buyer_contact": "Smith@gmail.com",
            "buyer_phone": "87654 32109",
            "buyer_tax_id": "GST987654321",
            "payment_terms": "Net 30",
            "items": [
                {
                    "description": "Laptop",
                    "quantity": 2,
                    "unit_price": 75000,
                    "amount": 150000,
                    "discount": 5000,
                    "tax_rate": 18,
                    "tax_amount": 27000,
                    "final_amount": 172000
                },
                {
                    "description": "Wireless Mouse",
                    "quantity": 3,
                    "unit_price": 1500,
                    "amount": 4500,
                    "discount": 200,
                    "tax_rate": 18,
                    "tax_amount": 774,
                    "final_amount": 5074
                }
            ]
        }
        return Response(dummy_invoice)
