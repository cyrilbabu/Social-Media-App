# Generated by Django 4.2.7 on 2023-11-17 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
