# Generated by Django 3.2.5 on 2022-04-02 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20220402_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_basket',
        ),
    ]