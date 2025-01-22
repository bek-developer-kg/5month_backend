from django.urls import path
from apps.settings.views import ProductCreateView, ProductListView, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name = "product_create"),
    path('product/list/', ProductListView.as_view(), name = "product_list"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(),name="product_delete"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(),name="product_update"),
]
