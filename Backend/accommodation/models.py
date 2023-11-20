from django.db import models


class AccommodationRequest(models.Model):
    def __repr__(self) -> str:
        return self.accommodation

    user = models.ForeignKey(
        "auth.User", related_name="accommodation_requests", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    accommodation = models.CharField(max_length=500)
