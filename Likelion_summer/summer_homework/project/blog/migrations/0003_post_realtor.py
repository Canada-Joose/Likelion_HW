# Generated by Django 4.0.6 on 2022-08-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='realtor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]