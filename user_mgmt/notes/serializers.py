from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    attachment_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Note
        fields = ["id", "title", "description", "attachment", "attachment_url", "created_at", "modified_at"]
        read_only_fields = ["created_at", "modified_at"]

    def get_attachment_url(self, obj):
        request = self.context.get("request")
        if obj.attachment and request is not None:
            return request.build_absolute_uri(obj.attachment.url)
        return None

    def create(self, validated_data):
        user = self.context["request"].user
        return Note.objects.create(owner=user, **validated_data)
