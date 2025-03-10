from django.urls import path
from .views import (
    InvoiceListCreateView, 
    InvoiceDetailView, 
    InvoiceDeleteAllView, 
    InvoiceDeleteByInvoiceNumberView
)

urlpatterns = [
    path("", InvoiceListCreateView.as_view(), name="invoice-list-create"),
    path("<invoice_number>/", InvoiceDetailView.as_view(), name="invoice-detail"),
    path("delete_all/", InvoiceDeleteAllView.as_view(), name="invoice-delete-all"),
    path("delete/<invoice_number>/", InvoiceDeleteByInvoiceNumberView.as_view(), name="invoice-delete-by-number"),
]
