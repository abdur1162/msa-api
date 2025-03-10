from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Invoice
from .serializers import InvoiceSerializer

# Custom pagination class (Optional: if you want to override settings.py)
class InvoicePagination(pagination.PageNumberPagination):
    page_size = 10  # Number of invoices per page
    page_size_query_param = "page_size"  # Allow dynamic page size via query parameter
    max_page_size = 100  # Limit maximum results per page

# GET all invoices with pagination, POST a new invoice
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = InvoicePagination  # Apply pagination

# GET a single invoice, PUT (update), DELETE by invoice_number
class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "invoice_number"  
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# DELETE all invoices
class InvoiceDeleteAllView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        Invoice.objects.all().delete()
        return Response({"message": "All invoices deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# DELETE a single invoice by invoice_number
class InvoiceDeleteByInvoiceNumberView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, invoice_number, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(invoice_number=invoice_number)
            invoice.delete()
            return Response({"message": f"Invoice {invoice_number} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
