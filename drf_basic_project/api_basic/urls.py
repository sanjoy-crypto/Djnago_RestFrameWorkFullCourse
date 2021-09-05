from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('articles', ArticleModelViewSet, basename='articles')
# router.register('articles', ArticleGenericViewSet, basename='articles')
# router.register('articles', ArticleViewSet, basename='articles')


urlpatterns = [

    # ------------Viewsets & Routers---------

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # -------------Generic-mixin VIew-------------

    # path('article/', GenericAPIView.as_view(), name="article"),
    # path('article/<int:id>/', GenericAPIView.as_view(), name="article_detail"),

    # ----------ClassView-----------

    # path('article/', ArticleAPIView.as_view(), name="article"),
    # path('article/<int:pk>/', articleDetailView.as_view(), name="article_detail"),

    # -----------FunctionView------------

    # path('article/', article_list, name="article"),
    # path('article/<int:pk>/', article_detail, name="article_detail"),
]
