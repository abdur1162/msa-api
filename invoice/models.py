from djongo import models

class Item(models.Model):
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    amount = models.FloatField()
    discount = models.FloatField()
    tax_rate = models.FloatField()
    tax_amount = models.FloatField()
    final_amount = models.FloatField()

    class Meta:
        abstract = True  # This is an embedded model (not a separate collection)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100, unique=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    seller_company_name = models.CharField(max_length=255)
    seller_address = models.TextField()
    seller_contact = models.EmailField()
    seller_phone = models.CharField(max_length=20)
    seller_tax_id = models.CharField(max_length=50)
    buyer_company_name = models.CharField(max_length=255)
    buyer_address = models.TextField()
    buyer_contact = models.EmailField()
    buyer_phone = models.CharField(max_length=20)
    buyer_tax_id = models.CharField(max_length=50)
    items = models.ArrayField(  # Store items as an array
        model_container=Item,
        null=True,
        blank=True
    )
    payment_terms = models.CharField(max_length=255)

    def __str__(self):
        return self.invoice_number
