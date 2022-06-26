
from rest_framework            import serializers
from arabic_keyword_api.models import keyword


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'keyword_text',
            'keyword_translations',
        )
        model = keyword

    def create(self, validated_data):
        return keyword.objects.create(**validated_data)
