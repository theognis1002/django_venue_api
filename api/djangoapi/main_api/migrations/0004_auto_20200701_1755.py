# Generated by Django 3.0.7 on 2020-07-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0003_auto_20200629_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
