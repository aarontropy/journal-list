from rest_framework import serializers
from models import JLCategory, JLItem

class JLCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JLCategory
        fields = ('id', 'category_text',)


class JLItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JLItem
        fields = ('id', 'url', 'item_text', 'pub_date',)
        depth = 1


class JLItemFullSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JLItem
        fields = ('id', 'url', 'category', 'item_text', 'pub_date',)
        depth = 1

class JLCategoryFullSerializer(serializers.HyperlinkedModelSerializer):
    items = JLItemSerializer(many=True)

    class Meta:
        model = JLCategory
        fields = ('id', 'category_text', 'items',)
    
