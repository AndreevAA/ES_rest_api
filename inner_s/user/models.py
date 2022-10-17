from django.db import models

from django.contrib.auth import get_user_model


User_t = get_user_model()


class User(models.Model):
    id = models.IntegerField('id')
    login = models.CharField('login', max_length=150, primary_key=True)
    password = models.CharField('password', max_length=150)
    acs_level = models.IntegerField('acs_level')

    class Meta:
        db_table = 'users'

