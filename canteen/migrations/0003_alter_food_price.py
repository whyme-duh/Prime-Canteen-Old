# Generated by Django 4.0.3 on 2022-04-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0002_remove_food_descriptions_remove_food_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(),
        ),
    ]
