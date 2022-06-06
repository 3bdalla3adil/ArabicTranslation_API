from django.shortcuts           import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework             import generics


from arabic_keyword_api         import models
from .serializers               import KeywordSerializer


class ListKeyword(generics.ListCreateAPIView):
    queryset         = models.keyword.objects.all()
    serializer_class = KeywordSerializer


class DetailKeyword(generics.RetrieveUpdateDestroyAPIView):
    queryset         = models.keyword.objects.all()
    serializer_class = KeywordSerializer
