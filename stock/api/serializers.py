from rest_framework import serializers
from stock.models import Category, Brand, Firm, Product, Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)     # default read_only=True
    user_id = serializers.IntegerField(write_only=True)
    firm = serializers.StringRelatedField(read_only=True)     # default read_only=True
    firm_id = serializers.IntegerField(write_only=True)
    # product = ProductSerializer(many=True)

    class Meta:
        model = Transaction
        fields = "__all__"
        # exclude = ("price_total",)
        read_only_fields = ("price_total",)

    def create(self, validated_data):

        quantity = validated_data['quantity']
        price = validated_data['price']
        validated_data['price_total'] = quantity * price
        transaction = Transaction.objects.create(**validated_data)
        transaction.save()
        return transaction

    def validate(self, data):
        transaction = data['transaction']
        product_id = data['product_id']
        quantity = data['quantity']
        stock = Product.objects.filter(id=product_id).values()

        if transaction == 'in':
            new_stock = stock[0]['stock'] + quantity
        
        elif quantity <= stock[0]['stock']:
            new_stock = stock[0]['stock'] - quantity
        
        else:
            new_stock = stock[0]['stock']
            raise serializers.ValidationError(
                {"quantity": "product stock quantity is not enough..."}
            )

        Product.objects.filter(id=product_id).update(stock=new_stock)

        return data
