from django.http import JsonResponse, Http404
from requests import Response
from rest_framework.decorators import api_view

from .models import Passport
from .serializers import PassportSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework import permissions


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all().order_by('passport_id')
    serializer_class = PassportSerializer


class PassportDetail(generics.RetrieveAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer

    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method PUT not allowed"})
    #
    #     try:
    #         instance = Passport.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exists"})
    #
    #     serializer = PassportSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})




