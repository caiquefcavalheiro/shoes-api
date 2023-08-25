from rest_framework import generics
from .models import SocialMedia
from .serializers import SocialMediaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class SocialMediaView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

    def get_queryset(self):
        return SocialMedia.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class SocialMediaViewId(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
