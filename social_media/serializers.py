from rest_framework import serializers
from .models import SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ["id", "social", "page_url", "user_id"]
        extra_kwargs = {"id": {"read_only": True}}
