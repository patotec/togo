# Generated by Django 2.2 on 2022-01-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='html_file',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
