# Generated by Django 4.0.6 on 2022-08-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
