from rest_framework import serializers
from .models import Invoice, Item

class ItemSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()
    unit_price = serializers.FloatField()
    amount = serializers.FloatField()
    discount = serializers.FloatField()
    tax_rate = serializers.FloatField()
    tax_amount = serializers.FloatField()
    final_amount = serializers.FloatField()

class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)  # Ensure items are handled as a list

    class Meta:
        model = Invoice
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])  # Extract items list
        invoice = Invoice.objects.create(**validated_data, items=items_data)
        return invoice

    def update(self, instance, validated_data):
        instance.invoice_number = validated_data.get("invoice_number", instance.invoice_number)
        instance.invoice_date = validated_data.get("invoice_date", instance.invoice_date)
        instance.due_date = validated_data.get("due_date", instance.due_date)
        instance.seller_company_name = validated_data.get("seller_company_name", instance.seller_company_name)
        instance.seller_address = validated_data.get("seller_address", instance.seller_address)
        instance.seller_contact = validated_data.get("seller_contact", instance.seller_contact)
        instance.seller_phone = validated_data.get("seller_phone", instance.seller_phone)
        instance.seller_tax_id = validated_data.get("seller_tax_id", instance.seller_tax_id)
        instance.buyer_company_name = validated_data.get("buyer_company_name", instance.buyer_company_name)
        instance.buyer_address = validated_data.get("buyer_address", instance.buyer_address)
        instance.buyer_contact = validated_data.get("buyer_contact", instance.buyer_contact)
        instance.buyer_phone = validated_data.get("buyer_phone", instance.buyer_phone)
        instance.buyer_tax_id = validated_data.get("buyer_tax_id", instance.buyer_tax_id)
        instance.items = validated_data.get("items", instance.items)  # Update items properly
        instance.payment_terms = validated_data.get("payment_terms", instance.payment_terms)
        instance.save()
        return instance
