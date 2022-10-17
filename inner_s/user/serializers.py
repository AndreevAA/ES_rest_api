from rest_framework import serializers

import db
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import permissions


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    login = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    acs_level = serializers.IntegerField(min_value=1, max_value=3)

    class Meta:
        model = User
        fields = ('id')

    @staticmethod
    def __is_all_fields_existed(fields, validated_data):
        for _ in fields:
            if not _ in validated_data:
                return False
        return True

    def create(self, validated_data):
        # Необходимые поля
        fields = ['login', 'password', 'acs_level']

        # Проверка на наличие всех необходимых полей
        if not self.__is_all_fields_existed(fields, validated_data):
            return Response(self.errors, status=status.HTTP_400_BAD_REQUEST)

        # Проверка наличия данного логина
        # if db.DB().is_user_login_existed(validated_data['login']):
        #     return Response(status=status.HTTP_403_FORBIDDEN)

        # Обработанные данные
        validated_data["id"] = db.DB().get_id_for_new_user()
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.acs_level = validated_data.get('acs_level', instance.acs_level)
        instance.save()
        return instance


