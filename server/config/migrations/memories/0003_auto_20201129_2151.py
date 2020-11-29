# Generated by Django 3.1.3 on 2020-11-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0002_auto_20201129_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='latitude',
            field=models.DecimalField(decimal_places=16, max_digits=23),
        ),
        migrations.AlterField(
            model_name='memory',
            name='longitude',
            field=models.DecimalField(decimal_places=16, max_digits=23),
        ),
    ]
