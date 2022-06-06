
from rest_framework     import serializers
from arabic_keyword_api import models


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'keyword_text',
        )
        model = models.keyword