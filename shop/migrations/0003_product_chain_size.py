# Generated by Django 3.2.5 on 2022-02-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220125_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='chain_size',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]