# Generated by Django 3.2.18 on 2023-04-11 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_decriptions_recipe_decription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='decription',
            new_name='description',
        ),
    ]