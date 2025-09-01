from django.db import models
from django.contrib.auth.models import User

def attachment_upload_to(instance, filename):
    return f"attachments/user_{instance.owner_id}/{filename}"

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    attachment = models.FileField(upload_to=attachment_upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_at"]

    def __str__(self):
        return f"{self.title} ({self.owner.username})"
