# Generated by Django 3.2.8 on 2021-10-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghsapp', '0003_auto_20211015_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='photos/default.png', null=True, upload_to='static/photos/'),
        ),
    ]