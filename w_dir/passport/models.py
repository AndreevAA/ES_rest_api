from django.db import models

from django.contrib.auth import get_user_model


User_t = get_user_model()


class Passport(models.Model):
    passport_id = models.IntegerField('passport_id', primary_key=True)
    name = models.CharField('name', max_length=150)
    surname = models.CharField('surname', max_length=150)
    patronymic = models.CharField('patronymic', max_length=150)
    registration = models.CharField('registration', max_length=150)
    children_number = models.IntegerField('children_number')
    is_married_now = models.BooleanField('is_married_now')
    birth_date = models.DateField('birth_date')
    is_depth = models.BooleanField('is_depth')
    depth_date = models.DateField('depth_date')

    class Meta:
        db_table = 'passports'

