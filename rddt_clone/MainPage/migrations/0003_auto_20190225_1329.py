# Generated by Django 2.1.5 on 2019-02-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_auto_20190218_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post'},
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='title'),
        ),
    ]
