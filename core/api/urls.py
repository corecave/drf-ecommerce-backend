from django.urls import path, include

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('products/', include('products.urls'))
]
