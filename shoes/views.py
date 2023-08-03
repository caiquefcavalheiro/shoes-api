from rest_framework import generics
from .models import Shoes
from .serializers import ShoesSerializer


class ShoesView(generics.ListCreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class ShoewViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
