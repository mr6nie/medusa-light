from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = News
        fields = ["date", "subject", "content"]
