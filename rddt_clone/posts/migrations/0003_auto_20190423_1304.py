# Generated by Django 2.2 on 2019-04-23 13:04

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='posts'),
        ),
    ]
