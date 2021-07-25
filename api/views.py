from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order.models import Order

from .serializers import OrderSerializer


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
