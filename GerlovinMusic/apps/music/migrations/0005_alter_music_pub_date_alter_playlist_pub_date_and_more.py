# Generated by Django 4.0.4 on 2022-06-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_concert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='verse',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
