from datetime import datetime

from rest_framework import serializers

from categories.serializers import CategorySerializer
from products.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source='productimage_set')
    is_sale = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)

    def get_is_sale(self, obj):
        if obj.sale_price > 0 and obj.sale_start_date is not None and obj.sale_start_date <= datetime.now().date() and (
                obj.sale_end_date is None or obj.sale_end_date >= datetime.now().date()):
            return True
        return False

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'images',
            'slug',
            'excerpt',
            'description',
            'category',
            'stock',
            'stock_limit',
            'price',
            'is_sale',
            'sale_price',
            'sale_start_date',
            'sale_end_date',
            'created_at',
            'updated_at',
        )
