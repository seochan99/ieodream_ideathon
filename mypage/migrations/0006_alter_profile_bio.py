# Generated by Django 3.2.5 on 2021-08-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0005_remove_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=10, null=True),
        ),
    ]