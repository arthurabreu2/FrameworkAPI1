from rest_framework.serializers import ModelSerializer
from frameworkapi.models import JsonPlaceholder

class JsonPlaceholderSerializer(ModelSerializer):
    class Meta:
        model = JsonPlaceholder
        fields = ('userId', 'id', 'title', 'completed')