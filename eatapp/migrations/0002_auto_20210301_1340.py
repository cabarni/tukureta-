# Generated by Django 3.1.7 on 2021-03-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatmodel',
            name='snsimage',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
