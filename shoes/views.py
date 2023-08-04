from rest_framework import generics
from .models import Shoes
from .serializers import ShoesSerializer
from rest_framework.response import Response


class ShoesView(generics.ListCreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer

    def get(self, request, *args, **kwargs):
        search_params = request.query_params.get("search")

        if search_params:
            shoes = Shoes.objects.filter(name=search_params)

            serializer = ShoesSerializer(shoes, many=True)
            return Response(serializer.data)

        return super().get(request, *args, **kwargs)


class ShoewViewId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
