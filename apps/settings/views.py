from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from apps.settings.models import Product
from apps.settings.serializer import ProductSerializer

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer