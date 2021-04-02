# Create your views here.
from rest_framework import filters, viewsets

from categories.models import Category
from products.models import Product
from products.serializers import ProductImageSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    search_fields = ('name', 'excerpt', 'description')

    def perform_create(self, serializer):
        self.process(serializer)

    def perform_update(self, serializer):
        self.process(serializer)

    def process(self, serializer):
        product = serializer.save()
        images = self.request.FILES.getlist('images')
        category = Category.objects.get(pk=self.request.data.get('category'))

        if category:
            product.category = category
            product.save()

        if images:
            for image in images:
                product_image_serializer = ProductImageSerializer(data={
                    'src': image,
                    'product': product.id
                })

                if product_image_serializer.is_valid():
                    product_image_serializer.save()
                else:
                    print(product_image_serializer.errors)
