from retail.apps import RetailConfig
from django.urls import path
from retail.views import SellerCreateApiView, SellerRetrieveApiView, SellerUpdateApiView, SellerDestroyApiView, \
    SellerListApiView

app_name = RetailConfig.name

urlpatterns = [
    path('seller/create/', SellerCreateApiView.as_view(), name='seller-create'),
    path('seller/list/', SellerListApiView.as_view(), name='seller-list'),
    path('seller/<int:pk>/', SellerRetrieveApiView.as_view(), name='seller-retrieve'),
    path('seller/<int:pk>/update/', SellerUpdateApiView.as_view(), name='seller-update'),
    path('seller/<int:pk>/delete/', SellerDestroyApiView.as_view(), name='seller-delete'),
]
