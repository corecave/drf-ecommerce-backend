from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    def get_parent(self, obj):
        return CategorySerializer(obj.parent).data if obj.parent else None

    class Meta:
        model = Category
        fields = '__all__'
