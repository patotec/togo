# Generated by Django 2.2 on 2022-01-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20220128_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='file',
            field=models.CharField(max_length=5000),
        ),
    ]
