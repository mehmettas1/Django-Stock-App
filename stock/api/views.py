from rest_framework import viewsets
from rest_framework import permissions
from stock.api.permissions import ProductManagerPermission
from stock.models import Category, Brand, Firm, Product, Transaction
from .serializers import CategorySerializer, FirmSerializer, BrandSerializer, TransactionSerializer, ProductSerializer
from django.db.models import Sum


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissions]


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [ProductManagerPermission]

    


