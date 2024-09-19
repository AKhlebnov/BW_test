from rest_framework import mixins, viewsets

from product.models import Product
from .serializers import ProductSerializer


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Класс представления для создания продукта и
    получиния списка продуктов.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
