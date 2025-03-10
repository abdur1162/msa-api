from django.urls import path
from .views import InvoiceDummyDataView

urlpatterns = [
    path('', InvoiceDummyDataView.as_view(), name='dummy-invoice'),
]
