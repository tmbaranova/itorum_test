from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from order.models import Order
from rest_framework import status


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

