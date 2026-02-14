from rest_framework import viewsets

from .models import Ship, Voyage
from .serializers import ShipSerializer, VoyageSerializer

# Create your views here.
class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

class VoyageViewSet(viewsets.ModelViewSet):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer