# Create your views here.
from rest_framework import viewsets, parsers

from products.models import Product
from products.serializers import ProductImageSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        product = serializer.save()
        images = self.request.FILES.getlist('images')

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



