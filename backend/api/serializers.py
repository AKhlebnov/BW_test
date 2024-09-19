from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продукта.
    """

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
        )

    def validate_price(self, value):
        # Показана проверка, хотя валидатор из модели уже это проверяет
        if value < 0:
            raise serializers.ValidationError(
                'Цена должна быть положительным числом.'
            )
        return value

    def validate_name(self, value):
        # Показана проверка, хотя валидатор из модели уже это проверяет
        if not value:
            raise serializers.ValidationError(
                'Поле "name" обязательное.'
            )
        return value
