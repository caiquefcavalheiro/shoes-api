from django.db import models


class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    social = models.CharField(max_length=55)
    page_url = models.CharField(max_length=255)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="social"
    )
