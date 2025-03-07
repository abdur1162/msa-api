from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = [JWTAuthentication]  # Ensure JWT Authentication
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_number"  # Search by invoice number
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
