# Generated by Django 4.1.3 on 2025-04-07 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_company_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company_staff',
        ),
    ]
