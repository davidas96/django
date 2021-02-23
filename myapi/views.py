from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics

from .serializers import HeroSerializers, CategorySerializers, BlogSerializers
from .models import Hero, Category, Blog

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


@api_view(['GET', 'POST', 'DELETE'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            categories = categories.filter(name=name)

        categories_serializer = CategorySerializers(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        categories_serializer = CategorySerializers(data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse(categories_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Category.objects.all().delete()
        return JsonResponse({'message': '{} Categories were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category_serializer = CategorySerializers(category)
        return JsonResponse(category_serializer.data)

    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializers(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(category_serializer.data)
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'Category was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class CategoryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    #def get(self, request, *args, **kwargs):
    #   return self.list(request, *args, **kwargs)

    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


class CategoryDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)