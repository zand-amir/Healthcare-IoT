# Generated by Django 3.2.9 on 2021-12-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelo', '0003_alter_accelo_id_of_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelo',
            name='labeled',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='accelo',
            name='pitch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='accelo',
            name='roll',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='accelo',
            name='yaw',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
