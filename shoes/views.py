from rest_framework import generics
from .models import Shoes
from .serializers import ShoesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ShoesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

    def get_queryset(self):
        search_params = self.request.query_params.get("search")
        queryset = Shoes.objects.all()
        if search_params is not None:
            queryset = queryset.filter(name__icontains=search_params)
        return queryset


class ShoewViewId(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
