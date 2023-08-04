from rest_framework import generics
from .models import Shoes
from .serializers import ShoesSerializer
from rest_framework.response import Response


class ShoesView(generics.ListCreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

    def get_queryset(self):
        search_params = self.request.query_params.get("search")
        queryset = Shoes.objects.all()
        if search_params is not None:
            queryset = queryset.filter(name__icontains=search_params)
        return queryset


class ShoewViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
