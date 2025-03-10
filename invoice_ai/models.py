# from django.db import models

# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=20, unique=True)
#     invoice_date = models.DateField()
#     due_date = models.DateField()
#     seller_company_name = models.CharField(max_length=255)
#     seller_address = models.TextField()
#     seller_contact = models.EmailField()
#     seller_phone = models.CharField(max_length=20)
#     seller_tax_id = models.CharField(max_length=50)
#     buyer_company_name = models.CharField(max_length=255)
#     buyer_address = models.TextField()
#     buyer_contact = models.EmailField()
#     buyer_phone = models.CharField(max_length=20)
#     buyer_tax_id = models.CharField(max_length=50)
#     payment_terms = models.CharField(max_length=50)

#     def __str__(self):
#         return self.invoice_number

# class InvoiceItem(models.Model):
#     invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
#     description = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     unit_price = models.FloatField()
#     amount = models.FloatField()
#     discount = models.FloatField(default=0)
#     tax_rate = models.FloatField(default=18)
#     tax_amount = models.FloatField()
#     final_amount = models.FloatField()

#     def __str__(self):
#         return self.description
