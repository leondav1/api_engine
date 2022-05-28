from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StoreSerializer, VisitSerializer
from .models import Store, Visit, tz


class StoreViewSet(viewsets.ViewSet):
    def list(self, request):
        phone = request.query_params.get('phone')
        queryset = Store.objects.all().select_related('worker').filter(worker__phone_number=phone)
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)


class VisitView(APIView):
    def get(self, request):
        visits = Visit.objects.all().select_related('store').select_related('store__worker').\
            filter(store__worker__phone_number=request.query_params.get('phone'))
        serialiser = VisitSerializer(visits, many=True)
        return Response(serialiser.data)

    def post(self, request):
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('store').worker.phone_number
            if self.request.query_params.get('phone') != phone:
                return Response(
                    {'error': 'You are not logged in'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            answer = serializer.save()
            return Response({
                'id': answer.id,
                'visited_at': format(answer.visited_at.astimezone(tz).strftime('%d-%m-%Y %H:%M'))
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

