from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'blog', views.BlogViewSet)

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    url(r'^api/categories$', views.category_list),
    url(r'^api/categories/(?P<pk>[0-9]+)$', views.category_detail),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]