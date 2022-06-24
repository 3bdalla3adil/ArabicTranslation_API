
from rest_framework     import serializers
from arabic_keyword_api import models


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'keyword_text',
<<<<<<< HEAD
            'keyword_translations',
=======
            'key_out_text',
>>>>>>> 8771cc18b1ab13e02f90578b7ddef2b7fc253895
        )
        model = models.keyword