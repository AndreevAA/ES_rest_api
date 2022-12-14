# Generated by Django 3.2.2 on 2022-10-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usr_acs_lvl',
            new_name='acs_lvl',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usr_login',
            new_name='login',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usr_psw',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usr_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
