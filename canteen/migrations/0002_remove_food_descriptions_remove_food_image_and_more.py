# Generated by Django 4.0.3 on 2022-04-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
        migrations.AddField(
            model_name='food',
            name='still_left',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='food',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
