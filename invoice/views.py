from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Invoice
from .serializers import InvoiceSerializer

# List & Create Invoice
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

# Retrieve, Update & Delete Invoice
class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_number"
    authentication_classes = [JWTAuthentication]  # Use JWT Authentication
    permission_classes = [permissions.IsAuthenticated]
