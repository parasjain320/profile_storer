# Generated by Django 2.2.5 on 2019-11-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20191125_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=160, null=True),
        ),
    ]