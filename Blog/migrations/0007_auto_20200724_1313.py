# Generated by Django 3.0.3 on 2020-07-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20200723_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
