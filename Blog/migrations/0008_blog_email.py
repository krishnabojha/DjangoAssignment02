# Generated by Django 3.0.3 on 2020-07-25 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20200724_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.AuthorDetail'),
        ),
    ]
