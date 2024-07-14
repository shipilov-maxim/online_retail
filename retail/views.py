from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter
from retail.models import Seller
from retail.serializers import SellerSerializer, SellerUpdateSerializer


class SellerApiViewMixin:
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class SellerCreateApiView(SellerApiViewMixin, CreateAPIView):
    pass


class SellerRetrieveApiView(SellerApiViewMixin, RetrieveAPIView):
    pass


class SellerUpdateApiView(SellerApiViewMixin, UpdateAPIView):
    serializer_class = SellerUpdateSerializer


class SellerDestroyApiView(SellerApiViewMixin, DestroyAPIView):
    pass


class SellerListApiView(SellerApiViewMixin, ListAPIView):
    filter_backends = [SearchFilter,]
    search_fields = ['seller_contact__city',]
