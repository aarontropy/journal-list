from rest_framework import serializers
from models import JLCategory, JLItem
from datetime import date

class JLCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JLCategory
        fields = ('id', 'url','category_text',)


class JLItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JLItem
        fields = ('id', 'url', 'item_text', 'pub_date', 'category')


class JLItemFullSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JLItem
        fields = ('id', 'url', 'category', 'item_text', 'pub_date',)
        depth = 1

class JLCategoryFullSerializer(serializers.HyperlinkedModelSerializer):
    items = JLItemSerializer(many=True)

    class Meta:
        model = JLCategory
        fields = ('id', 'url', 'category_text', 'items',)



class DailyItemsSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.SerializerMethodField('get_items_filtered_by_date')

    class Meta:
        model = JLCategory

    def get_items_filtered_by_date(self, obj):
        qs = JLItem.objects.filter(category=obj, pub_date=getattr(self.context['view'], 'date', date.today()) )
        return JLItemSerializer(qs, many=True, context={'request':self.context['request']}).data
    
