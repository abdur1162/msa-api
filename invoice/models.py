from djongo import models  # Use Djongo's models
from bson import ObjectId


class Invoice(models.Model):
    id = models.ObjectIdField(default=ObjectId, primary_key=True)
    invoice_number = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateField()
    due_date = models.DateField()

    # Seller details
    seller_company_name = models.CharField(max_length=255)
    seller_address = models.TextField()
    seller_contact = models.EmailField()
    seller_phone = models.CharField(max_length=20)
    seller_tax_id = models.CharField(max_length=50)

    # Buyer details
    buyer_company_name = models.CharField(max_length=255)
    buyer_address = models.TextField()
    buyer_contact = models.EmailField()
    buyer_phone = models.CharField(max_length=20)
    buyer_tax_id = models.CharField(max_length=50)

    # Invoice items (Fix here: Use Djongo's JSONField)
    items = models.JSONField()

    # Payment terms
    payment_terms = models.CharField(max_length=100)

    def __str__(self):
        return self.invoice_number
