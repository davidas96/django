from rest_framework import serializers

from .models import Hero, Category, Blog


class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BlogSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'name', 'description', 'text', 'category', 'date')
