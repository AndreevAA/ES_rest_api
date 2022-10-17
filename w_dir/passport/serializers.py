from rest_framework import serializers

import db
from .models import Passport

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import permissions


class PassportSerializer(serializers.Serializer):
    passport_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    surname = serializers.CharField(max_length=150)
    patronymic = serializers.CharField(max_length=150)
    registration = serializers.CharField(read_only=True)
    children_number = serializers.IntegerField(min_value=0)
    is_married_now = serializers.BooleanField()
    birth_date = serializers.DateField()
    is_depth = serializers.BooleanField()
    depth_date = serializers.DateField()

    class Meta:
        model = Passport
        fields = ('passport_id')

    @staticmethod
    def __is_all_fields_existed(fields, validated_data):
        for _ in fields:
            if not _ in validated_data:
                return False
        return True

    def create(self, validated_data):
        # Обработанные данные
        validated_data["passport_id"] = db.DB().get_id_for_new_passport()
        return Passport.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.passport_id = validated_data.get('passport_id', instance.passport_id)
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.patronymic = validated_data.get('registration', instance.registration)
        instance.patronymic = validated_data.get('children_number', instance.children_number)
        instance.patronymic = validated_data.get('is_married_now', instance.is_married_now)
        instance.patronymic = validated_data.get('birth_date', instance.birth_date)
        instance.patronymic = validated_data.get('is_depth', instance.is_depth)
        instance.patronymic = validated_data.get('depth_date', instance.depth_date)

        instance.save()
        return instance


