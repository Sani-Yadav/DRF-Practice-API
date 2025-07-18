from rest_framework import serializers
from .models import Students


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'